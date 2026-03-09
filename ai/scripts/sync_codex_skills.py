#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync LOVE20 skills from this repo into a Codex skills directory."
    )
    parser.add_argument(
        "--source",
        default=None,
        help="Source skills directory. Defaults to <repo>/ai/skills.",
    )
    parser.add_argument(
        "--target",
        default="~/.codex/skills",
        help="Target Codex skills directory. Defaults to ~/.codex/skills.",
    )
    parser.add_argument(
        "--mode",
        choices=("symlink", "copy"),
        default="symlink",
        help="Install mode. Symlink keeps the repo as the source of truth.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace existing skill directories with the synced versions.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned operations without changing the filesystem.",
    )
    return parser.parse_args()


def resolve_paths(args: argparse.Namespace) -> tuple[Path, Path]:
    repo_root = Path(__file__).resolve().parents[2]
    source = Path(args.source).expanduser().resolve() if args.source else (repo_root / "ai" / "skills").resolve()
    target = Path(args.target).expanduser().resolve()
    return source, target


def list_skill_dirs(source: Path) -> list[Path]:
    return sorted(
        path
        for path in source.iterdir()
        if path.is_dir() and not path.name.startswith(".") and (path / "SKILL.md").exists()
    )


def ensure_target(target: Path, dry_run: bool) -> None:
    if target.exists():
        return
    if dry_run:
        print(f"CREATE DIR {target}")
        return
    target.mkdir(parents=True, exist_ok=True)


def remove_path(path: Path, dry_run: bool) -> None:
    if dry_run:
        print(f"REMOVE {path}")
        return
    if path.is_symlink() or path.is_file():
        path.unlink()
        return
    shutil.rmtree(path)


def sync_symlink(source_dir: Path, target_dir: Path, force: bool, dry_run: bool) -> None:
    if target_dir.is_symlink():
        if target_dir.resolve() == source_dir.resolve():
            print(f"OK {target_dir} -> {source_dir}")
            return
        if not force:
            raise RuntimeError(f"{target_dir} points elsewhere. Use --force to replace it.")
        remove_path(target_dir, dry_run)
    elif target_dir.exists():
        if not force:
            raise RuntimeError(f"{target_dir} already exists. Use --force to replace it.")
        remove_path(target_dir, dry_run)

    if dry_run:
        print(f"SYMLINK {target_dir} -> {source_dir}")
        return
    target_dir.symlink_to(source_dir, target_is_directory=True)
    print(f"SYMLINKED {target_dir} -> {source_dir}")


def sync_copy(source_dir: Path, target_dir: Path, force: bool, dry_run: bool) -> None:
    if target_dir.exists() or target_dir.is_symlink():
        if not force:
            raise RuntimeError(f"{target_dir} already exists. Use --force to replace it.")
        remove_path(target_dir, dry_run)

    if dry_run:
        print(f"COPY {source_dir} -> {target_dir}")
        return
    shutil.copytree(source_dir, target_dir, symlinks=True)
    print(f"COPIED {source_dir} -> {target_dir}")


def main() -> int:
    args = parse_args()
    source, target = resolve_paths(args)

    if not source.exists():
        print(f"Source directory not found: {source}", file=sys.stderr)
        return 1

    skill_dirs = list_skill_dirs(source)
    if not skill_dirs:
        print(f"No skill directories found under {source}", file=sys.stderr)
        return 1

    ensure_target(target, args.dry_run)

    print(f"Source: {source}")
    print(f"Target: {target}")
    print(f"Mode:   {args.mode}")

    for skill_dir in skill_dirs:
        target_dir = target / skill_dir.name
        if args.mode == "symlink":
            sync_symlink(skill_dir, target_dir, args.force, args.dry_run)
        else:
            sync_copy(skill_dir, target_dir, args.force, args.dry_run)

    if args.dry_run:
        print("Dry run complete.")
    else:
        print("Sync complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
