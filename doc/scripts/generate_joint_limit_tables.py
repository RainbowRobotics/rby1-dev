#!/usr/bin/env python3
"""Generate the joint range / speed limit tables from the rby1-sdk URDF models.

The controller enforces the limits written in the robot model (URDF), so the
documentation must show those values rather than hand-copied numbers.

Usage:
    python3 scripts/generate_joint_limit_tables.py [--sdk ../external/rby1-sdk] [--out source/hardware/generated]
"""
from __future__ import annotations

import argparse
import math
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Model folder in rby1-sdk/models -> (page title, output file).
MODELS = {
    "rby1a": ("Model A", "joint_limits_a.md"),
    "rby1m": ("Model M", "joint_limits_m.md"),
    "rby1ub": ("Model UB", "joint_limits_ub.md"),
}

# Body part order used in the tables; joints not matching any prefix are skipped (wheels, grippers).
JOINT_ORDER = ("torso_", "right_arm_", "left_arm_", "head_")
# Joints without a numeric suffix sort first within their part (e.g. UB torso_hp before torso_5).


VERSION_FILE = re.compile(r"model_v(\d+)\.(\d+)\.urdf$")


@dataclass(frozen=True)
class JointLimit:
    lower_deg: int
    upper_deg: int
    velocity_deg_s: int

    def range_text(self) -> str:
        return f"{self.lower_deg}° ~ {self.upper_deg}°"

    def speed_text(self) -> str:
        return f"{self.velocity_deg_s}°/s"


def _deg(rad: str) -> int:
    return round(math.degrees(float(rad)))


def read_joint_limits(urdf: Path) -> dict[str, JointLimit]:
    limits: dict[str, JointLimit] = {}
    for joint in ET.parse(urdf).getroot().iter("joint"):
        name = joint.get("name", "")
        limit = joint.find("limit")
        if joint.get("type") != "revolute" or limit is None or not name.startswith(JOINT_ORDER):
            continue
        limits[name] = JointLimit(_deg(limit.get("lower")), _deg(limit.get("upper")), _deg(limit.get("velocity")))
    return limits


def sort_key(name: str) -> tuple[int, int]:
    prefix = next(i for i, p in enumerate(JOINT_ORDER) if name.startswith(p))
    suffix = name.rsplit("_", 1)[1]
    return prefix, int(suffix) if suffix.isdigit() else -1


def versioned_urdfs(model_dir: Path) -> dict[str, Path]:
    found = {}
    for urdf in sorted(model_dir.glob("urdf/model_v*.urdf")):
        m = VERSION_FILE.search(urdf.name)
        if m:
            found[f"v{m.group(1)}.{m.group(2)}"] = urdf
    if not found and (model_dir / "urdf" / "model.urdf").exists():
        return {"current": model_dir / "urdf" / "model.urdf"}  # model without hardware versions (e.g. UB)
    return dict(sorted(found.items(), key=lambda kv: tuple(int(x) for x in kv[0][1:].split("."))))


def merge_cell(per_version: dict[str, str]) -> str:
    """One value if all versions agree, otherwise 'v1.0–v1.1: a<br>v1.2: b' grouped by consecutive equal values."""
    groups: list[tuple[list[str], str]] = []
    for version, value in per_version.items():
        if groups and groups[-1][1] == value:
            groups[-1][0].append(version)
        else:
            groups.append(([version], value))
    if len(groups) == 1:
        return groups[0][1]
    label = lambda vs: vs[0] if len(vs) == 1 else f"{vs[0]}–{vs[-1]}"
    return "<br>".join(f"{label(vs)}: {value}" for vs, value in groups)


def render_model(title: str, urdfs: dict[str, Path], sdk_ref: str) -> str:
    per_version = {v: read_joint_limits(p) for v, p in urdfs.items()}
    joints = sorted({j for limits in per_version.values() for j in limits}, key=sort_key)
    lines = [
        f"#### {title}" + (f" ({', '.join(urdfs)})" if list(urdfs) != ["current"] else ""),
        "",
        "| Joint | Range | Max speed |",
        "| ----- | ----- | --------- |",
    ]
    for joint in joints:
        present = {v: lim[joint] for v, lim in per_version.items() if joint in lim}
        rng = merge_cell({v: l.range_text() for v, l in present.items()})
        spd = merge_cell({v: l.speed_text() for v, l in present.items()})
        lines.append(f"| `{joint}` | {rng} | {spd} |")
    files = ", ".join(f"`models/{p.parent.parent.name}/urdf/{p.name}`" for p in urdfs.values())
    lines += ["", f"Source: {files} in rby1-sdk {sdk_ref}.", ""]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--sdk", type=Path, default=ROOT.parent / "external" / "rby1-sdk")
    parser.add_argument("--sdk-ref", default=None, help="SDK version label shown in the source line (default: git describe)")
    parser.add_argument("--out", type=Path, default=ROOT / "source" / "hardware" / "generated")
    args = parser.parse_args()

    sdk_ref = args.sdk_ref
    if sdk_ref is None:
        import subprocess

        sdk_ref = subprocess.run(
            ["git", "-C", str(args.sdk), "describe", "--tags", "--always"], capture_output=True, text=True, check=True
        ).stdout.strip()

    args.out.mkdir(parents=True, exist_ok=True)
    header = "<!-- Generated by doc/scripts/generate_joint_limit_tables.py from the rby1-sdk URDF models. Do not edit. -->\n\n"
    for folder, (title, filename) in MODELS.items():
        urdfs = versioned_urdfs(args.sdk / "models" / folder)
        if not urdfs:
            raise SystemExit(f"no URDF found in {args.sdk / 'models' / folder}")
        out = args.out / filename
        out.write_text(header + render_model(title, urdfs, sdk_ref))
        print(f"[joint-limits] wrote {out}")

if __name__ == "__main__":
    main()
