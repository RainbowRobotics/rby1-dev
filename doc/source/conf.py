from __future__ import annotations
import os
import sys
import pathlib
import importlib
import shutil

# ── 환경변수에서 SDK 버전 수신 ──────────────────────────────────────
SDK_VERSION = os.getenv("SDK_VERSION", os.getenv("RBY1_SDK_VERSION", "dev"))
AVAILABLE_VERSIONS = os.getenv("AVAILABLE_VERSIONS", "dev").split()
VERSION_BASE_PREFIX = os.getenv("VERSION_BASE_PREFIX", "/")

# ── Project information ───────────────────────────────────────────────
project = "RB-Y1 Hardware & SDK Manual"
author = "Rainbow Robotics"
copyright = "2025, Rainbow Robotics"

# 문서 버전 표기는 SDK 기준
version = SDK_VERSION
release = SDK_VERSION
html_title = f"RB-Y1 Documentation"

# ── General configuration ─────────────────────────────────────────────
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
    "myst_parser",
    "breathe",
    "sphinx_copybutton",
    "sphinx_design",
]

templates_path = ["_templates"]
exclude_patterns = []

# Scaled image를 클릭했을 때 원본 이미지로 링크되는 동작 비활성화
html_scaled_image_link = False

# 헤딩 앵커 아이콘 설정 #
html_permalinks_icon = "#"

# ── MyST parser options ───────────────────────────────────────────────
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "linkify",
    "tasklist",
    "attrs_block",
]
myst_heading_anchors = 3

# ── Autodoc / Autosummary ─────────────────────────────────────────────
autosummary_generate = True
autosummary_imported_members = True
autodoc_member_order = "groupwise"
autodoc_typehints = "description"
autodoc_inherit_docstrings = True
add_module_names = False
autoclass_content = "class"
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "inherited-members": False,
    "show-inheritance": False,
}

# ── Intersphinx mapping ───────────────────────────────────────────────
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
}

# ── HTML Theme (Furo) ─────────────────────────────────────────────────
html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_js_files = ["sidebar-scroll-to-clicked.js"]
html_theme_options = {}

# 검색창 아래에 표시할 SDK 버전 컨텍스트
html_context = {
    "sdk_version": SDK_VERSION,
    "available_versions": AVAILABLE_VERSIONS,
    "version_base_prefix": VERSION_BASE_PREFIX,
}

# RST/Markdown 내에서 |sdk_version| 사용 가능
rst_epilog = f"""
.. |sdk_version| replace:: {SDK_VERSION}
"""

# ── Breathe (C++ from Doxygen XML) ────────────────────────────────────
ROOT = pathlib.Path(__file__).resolve().parent.parent
_breathe_xml = os.environ.get("DOXYGEN_XML", str(ROOT / "build" / "doxygen" / "xml"))
breathe_projects = {"rby1-sdk": _breathe_xml}
breathe_default_project = "rby1-sdk"
breathe_use_project_refids = True
breathe_domain_by_extension = {
    "h": "cpp",
    "hpp": "cpp",
    "hh": "cpp",
    "ipp": "cpp",
    "c": "c",
    "cc": "cpp",
    "cpp": "cpp",
}


# ── Pybind11 remap ───────────────────────────────────────────────────
def _remap_pybind_modules():
    try:
        import rby1_sdk
    except Exception:
        return

    def _patch_module_names(mod):
        for attr, obj in vars(mod).items():
            m = getattr(obj, "__module__", None)
            if isinstance(m, str) and m.startswith("rby1_sdk._bindings"):
                try:
                    obj.__module__ = m.replace("rby1_sdk._bindings", "rby1_sdk", 1)
                except Exception:
                    pass

    for sub in ("math", "upc", "dynamics"):
        try:
            smod = importlib.import_module(f"rby1_sdk.{sub}")
        except Exception:
            continue
        _patch_module_names(smod)


_remap_pybind_modules()


# ── Autodoc Hooks ─────────────────────────────────────────────────────
def _strip_bindings_in_signature(
    app, what, name, obj, options, signature, return_annotation
):
    def rep(s):
        return s.replace("._bindings", "") if s else s

    return rep(signature), rep(return_annotation)


def _strip_bindings_in_docstring(app, what, name, obj, options, lines):
    for i, line in enumerate(lines):
        lines[i] = line.replace("._bindings", "")

def _publish_doxygen_html(app, exception):
    if exception is not None or app.builder.name != "html":
        return

    source_dir = ROOT / "build" / "doxygen" / "html"
    if not source_dir.exists():
        return

    target_dir = pathlib.Path(app.outdir) / "sdk" / "cpp" / "raw-api"
    shutil.rmtree(target_dir, ignore_errors=True)
    shutil.copytree(source_dir, target_dir)

def setup(app):
    app.connect("autodoc-process-signature", _strip_bindings_in_signature)
    app.connect("autodoc-process-docstring", _strip_bindings_in_docstring)
    app.connect("build-finished", _publish_doxygen_html)