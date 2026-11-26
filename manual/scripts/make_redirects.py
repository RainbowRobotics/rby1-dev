#!/usr/bin/env python3
"""Write redirect pages for URLs of the previous manuals (VitePress 2025, Sphinx 2026) into manual/public/.

External pages (for example the rby1-sdk Python tutorial) still link to these URLs. Each redirect is a
small static HTML page with a relative target, so it works under any site base path.

Usage: python3 manual/scripts/make_redirects.py   (then commit manual/public/<paths>)
"""
from __future__ import annotations

import html
import os
from pathlib import Path

PUBLIC = Path(__file__).resolve().parent.parent / "public"

# old path (relative to the site root) -> new page (relative to the site root) or an absolute URL
REDIRECTS = {
    # VitePress manual (2025)
    "docs/development/getting-started/access-information.html": "getting-started/network-and-ports.html",
    "docs/development/getting-started/installation.html": "getting-started/sdk-install-and-state.html",
    "docs/development/getting-started/quick-start-guide.html": "getting-started/",
    "docs/development/getting-started/quick-start-guide-legacy.html": "getting-started/",
    "docs/development/getting-started/web-gui.html": "software/web-ui.html",
    "docs/development/rby1-sdk/controllers/command-and-control-architecture.html": "sdk/controllers/generated/command_and_control_architecture.html",
    "docs/development/rby1-sdk/controllers/control-hold-time-and-minimum-time.html": "sdk/controllers/generated/control_hold_time_and_minimum_time.html",
    "docs/development/rby1-sdk/models/A.html": "sdk/models/generated/model_a.html",
    "docs/development/rby1-sdk/models/M.html": "sdk/models/generated/model_m.html",
    "docs/development/rby1-sdk/models/T5.html": "sdk/models/",
    "docs/development/rby1-sdk/parameters.html": "sdk/controllers/generated/parameter.html",
    "docs/development/rby1-sdk/protos/protos-before-v0.2.0.html": "sdk/protos/",
    "docs/development/rby1-sdk/protos/protos-v0.2.1.html": "sdk/protos/",
    "docs/development/rby1-sdk/protos/protos-v0.3.0.html": "sdk/protos/",
    "docs/development/rby1-sdk/protos/protos-v0.4.0.html": "sdk/protos/",
    "docs/development/rby1-sdk/protos/protos-v0.5.0.html": "sdk/protos/",
    "docs/development/rby1-sdk/robot-and-command.html": "sdk/python/",
    "docs/development/rby1-sdk/robot-state.html": "sdk/python/",
    "docs/development/troubleshooting/build-issue.html": "sdk/troubleshooting/generated/build_issue.html",
    "docs/development/troubleshooting/error-reporting.html": "sdk/troubleshooting/generated/error_reporting.html",
    "docs/development/troubleshooting/faq.html": "sdk/troubleshooting/generated/faq.html",
    "docs/development/troubleshooting/robot_detaching_guide.html": "maintenance/detaching_guide.html",
    "docs/examples/cpp-examples.html": "examples/ex.html",
    "docs/examples/python-examples.html": "examples/ex.html",
    "docs/examples/python/demo_motion.html": "examples/ex.html",
    "docs/introduction/hello-rby1.html": "getting-started/hello_rby1.html",
    "docs/introduction/hw/battery-charger.html": "hardware/battery.html",
    "docs/introduction/hw/electrical-part.html": "hardware/electrical_part.html",
    "docs/introduction/hw/mechanical-part.html": "hardware/mechanical_part.html",
    "docs/introduction/hw/overview.html": "hardware/overview.html",
    "docs/introduction/options/gripper.html": "options/gripper.html",
    "docs/introduction/options/master-arm.html": "options/leader_arm.html",
    "docs/introduction/sw/index.html": "software/",
    "docs/introduction/sw/robot-main-program.html": "software/robot_main_program.html",
    "docs/introduction/sw/software-architecture.html": "software/architecture.html",
    "docs/rpc-release/index.html": "rpc_management_tools/rpc_updater.html",
    "docs/simulators/index.html": "simulators/",
    "README.html": "",
    "rby1-sdk/README.html": "sdk/",
    "rby1-sdk/CHANGELOG.html": "https://github.com/RainbowRobotics/rby1-sdk/blob/main/CHANGELOG.md",
    # Sphinx manual (2026): the misspelled troubleshooting folder
    "sdk/trobuleshooting/index.html": "sdk/troubleshooting/",
    "sdk/trobuleshooting/generated/build_issue.html": "sdk/troubleshooting/generated/build_issue.html",
    "sdk/trobuleshooting/generated/error_reporting.html": "sdk/troubleshooting/generated/error_reporting.html",
    "sdk/trobuleshooting/generated/faq.html": "sdk/troubleshooting/generated/faq.html",
    "sdk/trobuleshooting/fault-diagnosis.html": "sdk/troubleshooting/fault-diagnosis.html",
    # Sphinx manual (2026) pages that have no VitePress equivalent
    "genindex.html": "sdk/",
    "py-modindex.html": "sdk/python/",
    "search.html": "",
}

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Moved | RB-Y1</title>
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={url}">
<link rel="canonical" href="{url}">
</head>
<body>
<p>This page has moved to <a href="{url}">{label}</a>.</p>
</body>
</html>
"""


def relative_url(old: str, new: str) -> str:
    if new.startswith("http"):
        return new
    depth = old.count("/")
    return "../" * depth + new if (depth or new) else "./"


def main() -> None:
    for old, new in REDIRECTS.items():
        target = PUBLIC / old
        target.parent.mkdir(parents=True, exist_ok=True)
        url = relative_url(old, new)
        target.write_text(TEMPLATE.format(url=html.escape(url), label=html.escape(new or "the RB-Y1 manual")))
    print(f"[redirects] {len(REDIRECTS)} pages in {os.path.relpath(PUBLIC)}")


if __name__ == "__main__":
    main()
