#!/usr/bin/env python3
"""Check every link and #anchor between pages of the built site (VitePress only checks whole pages).

Usage: python manual/scripts/check_links.py manual/.vitepress/dist /rby1-dev/
Exits 1 when a link points to a missing page or a missing anchor.
"""
from __future__ import annotations

import html
import os
import re
import sys
from collections import Counter
from urllib.parse import unquote, urlparse

SKIP_DIRS = ("/raw-api",)  # Doxygen HTML: not part of the VitePress site


def main() -> int:
    root, base = sys.argv[1], sys.argv[2]
    os.chdir(root)
    pages = [os.path.relpath(os.path.join(d, f)) for d, _, fs in os.walk(".") for f in fs
             if f.endswith(".html") and not any(s in d for s in SKIP_DIRS)]
    ids: dict[str, set[str] | None] = {}

    def anchors(page: str) -> set[str] | None:
        if page not in ids:
            try:
                ids[page] = set(re.findall(r'\sid="([^"]+)"', open(page, errors="ignore").read()))
            except OSError:
                ids[page] = None
        return ids[page]

    missing_pages: dict[str, set[str]] = {}
    missing_anchors: dict[str, set[str]] = {}
    for page in pages:
        for href in re.findall(r'href="([^"]+)"', open(page, errors="ignore").read()):
            href = html.unescape(href)
            if href.startswith(("http", "mailto:", "javascript:", "tel:")) or href == "#":
                continue
            url = urlparse(href)
            path = unquote(url.path)
            if not path:
                target = page
            elif path.startswith(base):
                target = os.path.normpath(path[len(base):] or "index.html")
            elif path.startswith("/"):
                missing_pages.setdefault(path, set()).add(page)
                continue
            else:
                target = os.path.normpath(os.path.join(os.path.dirname(page), path))
            if os.path.isdir(target):
                target = os.path.join(target, "index.html")
            if not os.path.exists(target):
                missing_pages.setdefault(target, set()).add(page)
                continue
            if url.fragment and target.endswith(".html"):
                found = anchors(target)
                if found is not None and unquote(url.fragment) not in found:
                    missing_anchors.setdefault(f"{target}#{url.fragment}", set()).add(page)

    print(f"[links] {len(pages)} pages, {len(missing_pages)} missing targets, {len(missing_anchors)} missing anchors")
    for target, sources in sorted(missing_pages.items())[:50]:
        print(f"  missing page   {target}  <- {sorted(sources)[:3]}")
    by_page = Counter(k.split("#")[0] for k in missing_anchors)
    for target, n in by_page.most_common(50):
        examples = [k.split("#", 1)[1] for k in missing_anchors if k.startswith(target + "#")][:3]
        print(f"  missing anchor {target} x{n}: {examples}")
    return 1 if missing_pages or missing_anchors else 0


if __name__ == "__main__":
    sys.exit(main())
