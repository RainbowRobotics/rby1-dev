#!/usr/bin/env python3
"""Replace the content of a Pages branch checkout with a built site.

Versions: the site holds one version, the latest, at the root, so existing URLs keep working.
Older versions are not kept on the site (a build is about 360 MB and a GitHub Pages site is
limited to 1 GB; a VitePress build also hard-codes its base path, so a copy of it cannot be moved
to /<version>/). Earlier releases are listed on GitHub (see README, "배포와 버전").

Usage:
    python3 doc/scripts/publish_site.py --build manual/.vitepress/dist --site ../site --version v0.10.1
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

# Entries of the Pages branch that are not part of a build.
SITE_FILES = {".git", ".nojekyll", "CNAME"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--build", type=Path, required=True, help="built site (manual/.vitepress/dist)")
    parser.add_argument("--site", type=Path, required=True, help="checkout of the Pages branch")
    parser.add_argument("--version", required=True, help="SDK version the site documents, e.g. v0.10.1")
    args = parser.parse_args()

    if not re.fullmatch(r"v\d+\.\d+\.\d+([.-][0-9A-Za-z.]+)?", args.version):
        raise SystemExit(f"version must look like v1.2.3, got {args.version!r}")
    if not (args.build / "index.html").exists():
        raise SystemExit(f"{args.build} does not contain index.html")
    if not (args.site / ".git").exists():
        raise SystemExit(f"{args.site} is not a git checkout of the Pages branch")

    for entry in args.site.iterdir():
        if entry.name in SITE_FILES:
            continue
        if entry.is_dir() and not entry.is_symlink():
            shutil.rmtree(entry)
        else:
            entry.unlink()
    shutil.copytree(args.build, args.site, dirs_exist_ok=True)
    (args.site / ".nojekyll").touch()
    (args.site / "version.json").write_text(json.dumps({"sdk_version": args.version}) + "\n")
    print(f"[publish] {args.build} -> {args.site} (version {args.version})")


if __name__ == "__main__":
    main()
