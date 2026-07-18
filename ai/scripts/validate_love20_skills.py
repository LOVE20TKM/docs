#!/usr/bin/env python3
import json
import re
from pathlib import Path


EXPECTED_SKILL_NAMES = set(
    "love20-contract-playbooks love20-core-protocol love20-extension-dev love20-extension-patterns "
    "love20-frontend-bridge love20-frontend-dev love20-integration-dev love20-navigator love20-prompts "
    "love20-runbooks love20-selectors-and-errors love20-state-and-events love20-test-and-release".split()
)
SKILL_RE = re.compile(r'^---\nname: ([a-z0-9-]+)\ndescription: ("(?:[^"\\]|\\.)*")\n---\n')
OPENAI_FIELD_RE = re.compile(r'^  ([a-z0-9_-]+): ("(?:[^"\\]|\\.)*")$')


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    match = SKILL_RE.match((skill_dir / "SKILL.md").read_text())
    if not match:
        return [f"{skill_dir.name}: frontmatter must contain only name and quoted description"]

    name, raw_description = match.groups()
    description = json.loads(raw_description)
    if name != skill_dir.name:
        errors.append(f"{skill_dir.name}: frontmatter name is {name}")
    if len(name) > 64:
        errors.append(f"{name}: name exceeds 64 characters")
    if not description or len(description) > 1024 or "<" in description or ">" in description:
        errors.append(f"{name}: invalid description")

    openai_path = skill_dir / "agents" / "openai.yaml"
    if not openai_path.is_file():
        return [*errors, f"{name}: agents/openai.yaml not found"]
    lines = openai_path.read_text().splitlines()
    if not lines or lines[0] != "interface:":
        return [*errors, f"{name}: agents/openai.yaml must start with interface:"]
    fields = {}
    for line in lines[1:]:
        if line and not line.startswith(" "):
            break
        match = OPENAI_FIELD_RE.match(line)
        if match:
            fields[match.group(1)] = json.loads(match.group(2))
    missing = {"display_name", "short_description", "default_prompt"} - fields.keys()
    if missing:
        return [*errors, f"{name}: missing interface fields: {', '.join(sorted(missing))}"]

    short_description = fields["short_description"]
    if not fields["display_name"]:
        errors.append(f"{name}: display_name is empty")
    if not 25 <= len(short_description) <= 64:
        errors.append(f"{name}: short_description must be 25-64 characters")
    if f"${name}" not in fields["default_prompt"]:
        errors.append(f"{name}: default_prompt must mention ${name}")
    return errors


def main() -> int:
    skills_root = Path(__file__).resolve().parents[1] / "skills"
    skill_dirs = sorted(path for path in skills_root.iterdir() if (path / "SKILL.md").is_file())
    skill_names = {skill_dir.name for skill_dir in skill_dirs}
    errors = []
    if skill_names != EXPECTED_SKILL_NAMES:
        missing = sorted(EXPECTED_SKILL_NAMES - skill_names)
        unexpected = sorted(skill_names - EXPECTED_SKILL_NAMES)
        errors.append(f"Expected 13 named LOVE20 skills; missing={missing}, unexpected={unexpected}")
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    if errors:
        print("\n".join(f"ERROR {error}" for error in errors))
        return 1
    print(f"Validated {len(skill_dirs)} LOVE20 skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
