#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Symlink LOVE20 skills from this repo into Codex.")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = Path(__file__).resolve().parents[1] / "skills"
    codex_home = Path(os.environ.get("CODEX_HOME") or (Path.home() / ".codex")).expanduser()
    target = codex_home / "skills"
    skill_dirs = sorted(path for path in source.iterdir() if (path / "SKILL.md").is_file())

    if not skill_dirs:
        print(f"No skills found under {source}", file=sys.stderr)
        return 1

    print(f"Source: {source}\nTarget: {target}\nMode:   symlink")

    conflicts = []
    for source_dir in skill_dirs:
        target_dir = target / source_dir.name
        if target_dir.exists() or target_dir.is_symlink():
            if not (target_dir.is_symlink() and target_dir.resolve() == source_dir.resolve()):
                conflicts.append((source_dir, target_dir))
    if conflicts:
        for source_dir, target_dir in conflicts:
            print(f"Error: {target_dir} exists and does not point to {source_dir}", file=sys.stderr)
        return 1

    if not target.exists():
        if args.dry_run:
            print(f"CREATE DIR {target}")
        else:
            target.mkdir(parents=True)

    for source_dir in skill_dirs:
        target_dir = target / source_dir.name
        if target_dir.is_symlink() and target_dir.resolve() == source_dir.resolve():
            print(f"OK {target_dir} -> {source_dir}")
            continue
        if args.dry_run:
            print(f"SYMLINK {target_dir} -> {source_dir}")
        else:
            target_dir.symlink_to(source_dir, target_is_directory=True)
            print(f"SYMLINKED {target_dir} -> {source_dir}")

    print("Dry run complete." if args.dry_run else "Sync complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
