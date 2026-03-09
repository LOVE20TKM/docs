#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


FUNCTION_RE = re.compile(
    r"function\s+([A-Za-z0-9_]+)\s*\((.*?)\)\s*([^;{]*)[;{]",
    re.DOTALL,
)

SCRIPT_CATEGORY_ORDER = [
    "setup",
    "launch",
    "stake",
    "submit",
    "vote",
    "join",
    "random",
    "verify",
    "mint",
    "token",
    "weth",
    "misc",
]

SCRIPT_DESCRIPTIONS = {
    "000_init": "load network-specific environment",
    "101_flow_all": "run the packaged end-to-end cast flow",
    "burnForParentToken": "redeem LOVE20 tokens for parent pool assets",
    "join": "join an action or add action stake",
    "join_query": "inspect join state",
    "join_update": "update action verification info",
    "join_withdraw": "withdraw from an action",
    "launch_claim": "claim fair-launch allocation and refund",
    "launch_contribute": "contribute to a fair launch",
    "launch_deploy": "deploy or start a launch",
    "launch_query": "inspect launch state",
    "launch_stat": "inspect launch statistics",
    "launch_withdraw": "withdraw a launch contribution before close",
    "mint_action_reward": "mint an action reward",
    "mint_gov_reward": "mint a governance reward",
    "mint_query": "inspect reward state",
    "random": "trigger random-account preparation or related flow",
    "random_query": "inspect randomness state",
    "stake_liquidity": "stake LP-backed liquidity",
    "stake_query": "inspect stake state",
    "stake_token": "stake token-only balance",
    "stake_unstake": "request unstake",
    "stake_withdraw": "withdraw after unstake delay",
    "submit": "submit an existing action for voting",
    "submit_new_action": "create and submit a new action",
    "submit_query": "inspect submit state",
    "token_query": "inspect token state",
    "verify": "submit verification scores",
    "verify_query": "inspect verification state",
    "vote": "vote on actions",
    "vote_query": "inspect vote state",
    "weth_deposit": "wrap native asset into WETH-style token",
    "weth_query": "inspect wrapped native token state",
    "weth_stat": "inspect wrapped token statistics",
    "weth_withdraw": "unwrap WETH-style token",
}

CORE_WRITE_INTERFACES = [
    "ILOVE20Launch.sol",
    "ILOVE20Stake.sol",
    "ILOVE20Submit.sol",
    "ILOVE20Vote.sol",
    "ILOVE20Join.sol",
    "ILOVE20Verify.sol",
    "ILOVE20Mint.sol",
    "ILOVE20Token.sol",
]


def collapse_ws(value: str) -> str:
    return " ".join(value.replace("\n", " ").split())


def parse_functions(content: str) -> list[dict[str, str]]:
    functions: list[dict[str, str]] = []
    for match in FUNCTION_RE.finditer(content):
        name, args, trailer = match.groups()
        kind = "read" if re.search(r"\b(view|pure)\b", trailer) else "write"
        functions.append(
            {
                "name": name,
                "args": collapse_ws(args),
                "kind": kind,
            }
        )
    return functions


def format_signature(function: dict[str, str]) -> str:
    args = function["args"]
    if args:
        return f'{function["name"]}({args})'
    return f'{function["name"]}()'


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


def script_category(stem: str) -> str:
    if stem in {"000_init", "101_flow_all"}:
        return "setup"
    if stem == "burnForParentToken":
        return "token"
    prefix = stem.split("_", 1)[0]
    if prefix in {"launch", "stake", "submit", "vote", "join", "random", "verify", "mint", "token", "weth"}:
        return prefix
    return "misc"


def render_periphery_contracts(
    periphery_src_dir: Path, periphery_root: Path
) -> list[str]:
    lines = ["## Periphery Helper Contracts", ""]
    for path in sorted(periphery_src_dir.glob("*.sol")):
        functions = [
            function
            for function in parse_functions(path.read_text())
            if not function["name"].startswith("_") and function["name"] != "init"
        ]
        reads = [item for item in functions if item["kind"] == "read"]
        writes = [item for item in functions if item["kind"] == "write"]

        lines.append(f"### {path.stem}")
        lines.append("")
        lines.append(f"- File: `{repo_path(path, periphery_root, 'periphery')}`")
        if reads:
            lines.append("- Reads:")
            for function in reads:
                lines.append(f"  - `{format_signature(function)}`")
        if writes:
            lines.append("- Writes:")
            for function in writes:
                lines.append(f"  - `{format_signature(function)}`")
        lines.append("")
    return lines


def render_core_write_surfaces(
    core_interfaces_dir: Path, core_root: Path
) -> list[str]:
    lines = ["## Core Write Surfaces", ""]
    for file_name in CORE_WRITE_INTERFACES:
        path = core_interfaces_dir / file_name
        functions = parse_functions(path.read_text())
        writes = [item for item in functions if item["kind"] == "write"]
        if path.stem == "ILOVE20Token":
            writes = [item for item in writes if item["name"] == "burnForParentToken"]
        lines.append(f"### {path.stem}")
        lines.append("")
        lines.append(f"- File: `{repo_path(path, core_root, 'core')}`")
        for function in writes:
            lines.append(f"- `{format_signature(function)}`")
        lines.append("")
    return lines


def render_scripts(cast_dir: Path) -> list[str]:
    grouped: dict[str, list[Path]] = {category: [] for category in SCRIPT_CATEGORY_ORDER}
    for path in sorted(cast_dir.glob("*.sh")):
        grouped[script_category(path.stem)].append(path)

    lines = ["## Cast Scripts", ""]
    for category in SCRIPT_CATEGORY_ORDER:
        paths = grouped[category]
        if not paths:
            continue
        lines.append(f"### {category}")
        lines.append("")
        for path in paths:
            description = SCRIPT_DESCRIPTIONS.get(path.stem, "existing LOVE20 cast helper")
            lines.append(f"- `{path.name}`: {description}")
        lines.append("")
    return lines


def main() -> None:
    docs_root = Path(__file__).resolve().parents[4]
    periphery_root = resolve_repo(docs_root.parent, "periphery")
    core_root = resolve_repo(docs_root.parent, "core")
    script_root = resolve_repo(docs_root.parent, "script")
    output_path = docs_root / "ai" / "skills" / "love20-contract-playbooks" / "references" / "generated-playbook-index.md"

    lines = [
        "# Generated Playbook Index",
        "",
        "This file is generated by `ai/skills/love20-contract-playbooks/scripts/generate_playbook_index.py`.",
        "Regenerate it after updating periphery helpers, core interfaces, or cast scripts.",
        "",
    ]
    lines.extend(render_periphery_contracts(periphery_root / "src", periphery_root))
    lines.extend(render_core_write_surfaces(core_root / "src" / "interfaces", core_root))
    lines.extend(render_scripts(script_root / "script" / "cast"))

    output_path.write_text("\n".join(lines).rstrip() + "\n")


if __name__ == "__main__":
    main()
