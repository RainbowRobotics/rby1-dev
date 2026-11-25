#!/usr/bin/env python3
"""Place a built HTML tree into a checkout of the Pages branch and update versions.json.

Site layout (keeps every existing URL working):
    /                  latest version (same paths as before versioning)
    /<version>/        older versions kept for reference, e.g. /v0.10.1/
    /versions.json     list read by the version switcher

The latest version is stored only once, at the root: one build is about 400 MB and
GitHub Pages sites are limited to 1 GB. When a new latest is published, pass
--archive-previous to keep the previous latest under /<its version>/.

Usage:
    # new latest release (previous latest moved to /<old version>/)
    python3 scripts/publish_site.py --build build/html/v0.11.0 --site ../site --version v0.11.0 --latest --archive-previous
    # older version only
    python3 scripts/publish_site.py --build build/html/v0.10.1 --site ../site --version v0.10.1
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

VERSION_DIR = re.compile(r"^v\d+\.\d+\.\d+([.-][0-9A-Za-z.]+)?$")
# Root entries that belong to the site, not to the latest build.
SITE_FILES = {".git", ".nojekyll", "CNAME", "versions.json"}


def _version_key(name: str) -> tuple[int, ...]:
    return tuple(int(x) for x in re.findall(r"\d+", name)[:3])


def _remove(path: Path) -> None:
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    else:
        path.unlink()


def _copy_tree(src: Path, dst: Path) -> None:
    shutil.copytree(src, dst, dirs_exist_ok=True)


def replace_root(build: Path, site: Path) -> None:
    """Make the site root equal to `build`, keeping version folders and site files."""
    for entry in site.iterdir():
        if entry.name in SITE_FILES or (entry.is_dir() and VERSION_DIR.match(entry.name)):
            continue
        _remove(entry)
    _copy_tree(build, site)


def write_versions(site: Path, base_url: str, latest: str | None) -> list[dict]:
    old = site / "versions.json"
    previous = json.loads(old.read_text()) if old.exists() else []
    if latest is None:
        latest = next((v["version"] for v in previous if v.get("preferred")), None)
    archived = {p.name for p in site.iterdir() if p.is_dir() and VERSION_DIR.match(p.name)}
    versions = sorted(archived | ({latest} if latest else set()), key=_version_key, reverse=True)
    entries = []
    for v in versions:
        is_latest = v == latest
        entries.append({
            "name": f"{v} (latest)" if is_latest else v,
            "version": v,
            # The latest version is served from the root so that existing links keep working.
            "url": base_url if is_latest else f"{base_url}{v}/",
            **({"preferred": True} if is_latest else {}),
        })
    old.write_text(json.dumps(entries, indent=2) + "\n")
    return entries


def current_latest(site: Path) -> str | None:
    old = site / "versions.json"
    if not old.exists():
        return None
    return next((v["version"] for v in json.loads(old.read_text()) if v.get("preferred")), None)


def archive_root(site: Path, version: str) -> None:
    """Copy the current root build (without other versions) to /<version>/."""
    target = site / version
    if target.exists():
        _remove(target)
    target.mkdir()
    for entry in site.iterdir():
        if entry.name in SITE_FILES or entry == target or (entry.is_dir() and VERSION_DIR.match(entry.name)):
            continue
        if entry.is_dir():
            shutil.copytree(entry, target / entry.name)
        else:
            shutil.copy2(entry, target / entry.name)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--build", type=Path, required=True, help="built HTML directory")
    parser.add_argument("--site", type=Path, required=True, help="checkout of the Pages branch")
    parser.add_argument("--version", required=True, help="version label, e.g. v0.10.1")
    parser.add_argument("--latest", action="store_true", help="publish this build at the site root")
    parser.add_argument("--archive-previous", action="store_true",
                        help="with --latest: keep the previous latest under /<its version>/")
    parser.add_argument("--base-url", default="https://rainbowrobotics.github.io/rby1-dev/")
    args = parser.parse_args()

    if not VERSION_DIR.match(args.version):
        raise SystemExit(f"version must look like v1.2.3, got {args.version!r}")
    if not (args.build / "index.html").exists():
        raise SystemExit(f"{args.build} does not contain index.html")
    if not args.site.is_dir():
        raise SystemExit(f"{args.site} is not a directory")
    if args.archive_previous and not args.latest:
        raise SystemExit("--archive-previous needs --latest")
    base_url = args.base_url if args.base_url.endswith("/") else args.base_url + "/"

    if args.latest:
        previous = current_latest(args.site)
        if args.archive_previous and previous and previous != args.version:
            archive_root(args.site, previous)
            print(f"[publish] archived previous latest {previous} -> /{previous}/")
        stale = args.site / args.version  # the new latest lives at the root only
        if stale.exists():
            _remove(stale)
        replace_root(args.build, args.site)
    else:
        version_dir = args.site / args.version
        if version_dir.exists():
            _remove(version_dir)
        _copy_tree(args.build, version_dir)
    (args.site / ".nojekyll").touch()

    entries = write_versions(args.site, base_url, args.version if args.latest else None)
    print(f"[publish] {args.version} -> " + ("site root" if args.latest else f"/{args.version}/"))
    print(f"[publish] versions.json: {[e['name'] for e in entries]}")


if __name__ == "__main__":
    main()
