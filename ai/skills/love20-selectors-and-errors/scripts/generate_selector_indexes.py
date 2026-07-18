#!/usr/bin/env python3
from __future__ import annotations

import ast
import json
import re
import shutil
import subprocess
from functools import cache
from pathlib import Path
from typing import Iterable


ERROR_MESSAGE_RE = re.compile(r"^\s*([A-Za-z0-9_]+):\s*(.+?),\s*$")


def read_json(path: Path) -> dict | list:
    return json.loads(path.read_text())


def normalize_message(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith(("'", '"', "`")) and raw.endswith(("'", '"', "`")):
        raw = raw[1:-1]
    return raw


def load_error_messages(path: Path) -> dict[str, str]:
    messages: dict[str, str] = {}
    for line in path.read_text().splitlines():
        match = ERROR_MESSAGE_RE.match(line)
        if not match:
            continue
        name, raw_message = match.groups()
        messages[name] = normalize_message(raw_message)
    return messages


def canonical_type(item: dict[str, object]) -> str:
    type_name = str(item["type"])
    if type_name.startswith("tuple"):
        components = ",".join(canonical_type(component) for component in item["components"])
        return f"({components}){type_name[len('tuple'):]}"
    return type_name


def abi_signature(name: str, inputs: list[dict[str, object]], source: bool = False) -> str:
    types = (str(item["type"]) if source else canonical_type(item) for item in inputs)
    return f'{name}({",".join(types)})'


def canonical_function_signature(row: dict[str, str], abi_root: Path) -> str:
    if "tuple" not in row["signature"]:
        return row["signature"]
    content = (abi_root / f'{row["contract"]}.ts').read_text()
    raw = content[content.index("[") : content.rindex("]") + 1]
    try:
        abi = json.loads(raw)
    except json.JSONDecodeError:
        abi = ast.literal_eval(raw)
    for item in abi:
        if item.get("type") != "function" or item.get("name") != row["functionName"]:
            continue
        inputs = [input_item for input_item in item.get("inputs", []) if isinstance(input_item, dict)]
        if abi_signature(str(item["name"]), inputs, source=True) == row["signature"]:
            return abi_signature(str(item["name"]), inputs)
    raise RuntimeError(f"No ABI match for {row['contract']} {row['signature']}")


def function_selector_rows(path: Path, frontend_abi_root: Path) -> list[dict[str, str]]:
    rows = read_json(path)
    assert isinstance(rows, list)
    seen: dict[tuple[str, str, str], set[str]] = {}
    for row in rows:
        signature = canonical_function_signature(row, frontend_abi_root)
        selector = keccak_hex(signature)[:10]
        seen.setdefault((selector, signature, row["functionName"]), set()).add(row["contract"])
    return [
        {
            "selector": selector,
            "contracts": ", ".join(sorted(contracts)),
            "functionName": name,
            "signature": signature,
        }
        for (selector, signature, name), contracts in sorted(seen.items())
    ]


@cache
def keccak_hex(signature: str) -> str:
    return subprocess.check_output(["cast", "keccak", signature], text=True).strip()


def error_rows(abi_root: Path, error_messages: dict[str, str]) -> list[dict[str, str]]:
    seen: dict[tuple[str, str], dict[str, str]] = {}
    for json_path in sorted(abi_root.glob("*/*.json")):
        payload = read_json(json_path)
        abi = payload.get("abi", []) if isinstance(payload, dict) else []
        contract = json_path.parent.name.replace(".sol", "")
        for item in abi:
            if item.get("type") != "error":
                continue
            inputs = [input_item for input_item in item.get("inputs", []) if isinstance(input_item, dict)]
            signature = abi_signature(str(item["name"]), inputs)
            selector = keccak_hex(signature)[:10]
            key = (selector, signature)
            if key not in seen:
                seen[key] = {
                    "selector": selector,
                    "name": item["name"],
                    "signature": signature,
                    "contracts": contract,
                    "message": error_messages.get(item["name"], item["name"]),
                }
            else:
                contracts = set(seen[key]["contracts"].split(", "))
                contracts.add(contract)
                seen[key]["contracts"] = ", ".join(sorted(contracts))
    return sorted(seen.values(), key=lambda row: (row["selector"], row["name"]))


def event_rows(abi_root: Path) -> list[dict[str, str]]:
    seen: dict[tuple[str, str], dict[str, str]] = {}
    for json_path in sorted(abi_root.glob("*/*.json")):
        payload = read_json(json_path)
        abi = payload.get("abi", []) if isinstance(payload, dict) else []
        contract = json_path.parent.name.replace(".sol", "")
        for item in abi:
            if item.get("type") != "event":
                continue
            inputs = [input_item for input_item in item.get("inputs", []) if isinstance(input_item, dict)]
            signature = abi_signature(str(item["name"]), inputs)
            topic0 = keccak_hex(signature)
            indexed_inputs = [input_item["name"] or "(anonymous)" for input_item in item.get("inputs", []) if input_item.get("indexed")]
            key = (topic0, signature)
            if key not in seen:
                seen[key] = {
                    "topic0": topic0,
                    "name": item["name"],
                    "signature": signature,
                    "contracts": contract,
                    "indexed": ", ".join(indexed_inputs) if indexed_inputs else "(none)",
                }
            else:
                contracts = set(seen[key]["contracts"].split(", "))
                contracts.add(contract)
                seen[key]["contracts"] = ", ".join(sorted(contracts))
    return sorted(seen.values(), key=lambda row: (row["topic0"], row["name"]))


def render_markdown(
    title: str,
    intro_lines: Iterable[str],
    rows: Iterable[dict[str, str]],
    columns: list[tuple[str, str]],
) -> str:
    lines = [f"# {title}", ""]
    lines.extend(intro_lines)
    lines.append("")
    lines.append("| " + " | ".join(label for _, label in columns) + " |")
    lines.append("| " + " | ".join("---" for _ in columns) + " |")
    for row in rows:
        values = []
        for key, _ in columns:
            value = str(row[key]).replace("\n", " ").replace("|", "\\|")
            values.append(value)
        lines.append("| " + " | ".join(values) + " |")
    lines.append("")
    return "\n".join(lines)


def resolve_repo(repo_parent: Path, canonical_name: str) -> Path:
    candidates = [canonical_name, f"LOVE20-{canonical_name}"]
    for candidate in candidates:
        path = repo_parent / candidate
        if path.exists():
            return path
    raise FileNotFoundError(
        f"Could not locate repo '{canonical_name}' or 'LOVE20-{canonical_name}' under {repo_parent}"
    )


def repo_path(path: Path, repo_root: Path, display_name: str) -> str:
    resolved = path.resolve()
    try:
        return f"{display_name}/{resolved.relative_to(repo_root.resolve())}"
    except ValueError:
        return str(resolved)


def main() -> None:
    if shutil.which("cast") is None:
        raise RuntimeError("Foundry 'cast' is required to generate selector indexes")

    docs_root = Path(__file__).resolve().parents[4]
    interface_root = resolve_repo(docs_root.parent, "interface-test")
    script_root = resolve_repo(docs_root.parent, "script")
    references_root = docs_root / "ai" / "skills" / "love20-selectors-and-errors" / "references"

    function_rows = function_selector_rows(
        interface_root / "docs" / "function-selectors.json",
        interface_root / "src" / "abis",
    )
    error_message_map = load_error_messages(interface_root / "src" / "errors" / "errorMessages.ts")
    error_rows_data = error_rows(script_root / "abi", error_message_map)
    event_rows_data = event_rows(script_root / "abi")

    function_md = render_markdown(
        "Generated Function Selector Index",
        [
            "This file is generated by `ai/skills/love20-selectors-and-errors/scripts/generate_selector_indexes.py`.",
            f"The source contract catalog is `{repo_path(interface_root / 'docs' / 'function-selectors.json', interface_root, 'interface-test')}`; tuple signatures are expanded from frontend ABI modules and all selectors are recomputed with `cast keccak`. Rows sharing a selector and signature are grouped by contract.",
        ],
        function_rows,
        [
            ("selector", "Selector"),
            ("contracts", "Contracts"),
            ("functionName", "Function"),
            ("signature", "Signature"),
        ],
    )

    error_md = render_markdown(
        "Generated Error Selector Index",
        [
            "This file is generated by `ai/skills/love20-selectors-and-errors/scripts/generate_selector_indexes.py`.",
            f"Selectors are computed from `{repo_path(script_root / 'abi', script_root, 'script')}/**/*Errors.json` and messages come from `{repo_path(interface_root / 'src' / 'errors' / 'errorMessages.ts', interface_root, 'interface-test')}`.",
        ],
        error_rows_data,
        [
            ("selector", "Selector"),
            ("name", "Error"),
            ("signature", "Signature"),
            ("contracts", "Contracts"),
            ("message", "Frontend Message"),
        ],
    )

    event_md = render_markdown(
        "Generated Event Topic Index",
        [
            "This file is generated by `ai/skills/love20-selectors-and-errors/scripts/generate_selector_indexes.py`.",
            f"Topic0 values are computed from `{repo_path(script_root / 'abi', script_root, 'script')}/**/*Events.json` using keccak.",
        ],
        event_rows_data,
        [
            ("topic0", "Topic0"),
            ("name", "Event"),
            ("signature", "Signature"),
            ("contracts", "Contracts"),
            ("indexed", "Indexed Inputs"),
        ],
    )

    (references_root / "generated-function-selector-index.md").write_text(function_md)
    (references_root / "generated-error-selector-index.md").write_text(error_md)
    (references_root / "generated-event-topic-index.md").write_text(event_md)


if __name__ == "__main__":
    main()
