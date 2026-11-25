from __future__ import annotations
import os
import sys
import pathlib
import importlib
import shutil
import datetime

# ── 환경변수에서 SDK 버전 수신 ──────────────────────────────────────
def _submodule_sdk_version() -> str:
    """Tag of the rby1-sdk submodule the API reference is generated from (e.g. v0.10.1)."""
    import subprocess

    sdk_dir = pathlib.Path(__file__).resolve().parents[2] / "external" / "rby1-sdk"
    try:
        return subprocess.run(
            ["git", "-C", str(sdk_dir), "describe", "--tags", "--always"],
            capture_output=True, text=True, check=True,
        ).stdout.strip() or "dev"
    except (OSError, subprocess.CalledProcessError):
        return "dev"


SDK_VERSION = os.getenv("SDK_VERSION", os.getenv("RBY1_SDK_VERSION")) or _submodule_sdk_version()

# ── Project information ───────────────────────────────────────────────
project = "RB-Y1 Hardware & SDK Manual"
author = "Rainbow Robotics"
copyright = f"2024-{datetime.date.today().year}, Rainbow Robotics"

# 문서 버전 표기는 SDK 기준
version = SDK_VERSION
release = SDK_VERSION

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
    "sphinxcontrib.mermaid",
]

templates_path = []  # the theme needs no template overrides
# Fragments pulled in with {include}; not pages of their own.
exclude_patterns = ["hardware/generated/*"]

# Scaled image를 클릭했을 때 원본 이미지로 링크되는 동작 비활성화
html_scaled_image_link = False

# 라이브 사이트와 같게: 헤딩 앵커는 기본 아이콘(¶), 페이지 소스 보기 링크는 숨김
html_show_sourcelink = False

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

# ── HTML Theme (PyData Sphinx Theme) ──────────────────────────────────
# Same layout family as the NVIDIA Isaac Sim docs (top section tabs, section sidebar,
# page table of contents on the right), using the BSD-licensed base theme.
DOCS_BASE_URL = os.getenv("DOCS_BASE_URL", "https://rainbowrobotics.github.io/rby1-dev/")

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_logo = "_static/images/brand/rb_logo.png"
html_favicon = "_static/images/brand/rb_logo.png"
html_title = "RB-Y1 Documentation"
html_baseurl = DOCS_BASE_URL
html_last_updated_fmt = "%Y-%m-%d"
html_theme_options = {
    "logo": {"text": "RB-Y1 Docs"},
    "navbar_align": "left",
    "header_links_before_dropdown": 8,
    "navbar_end": ["version-switcher", "theme-switcher", "navbar-icon-links"],
    "navbar_persistent": ["search-button"],
    "secondary_sidebar_items": ["page-toc", "edit-this-page"],
    "show_toc_level": 2,
    "show_prev_next": True,
    "use_edit_page_button": True,
    "icon_links": [
        {"name": "rby1-sdk", "url": "https://github.com/RainbowRobotics/rby1-sdk", "icon": "fa-brands fa-github"},
    ],
    # versions.json at the site root lists the published versions (see doc/scripts/publish_site.sh).
    "switcher": {"json_url": DOCS_BASE_URL + "versions.json", "version_match": SDK_VERSION},
    "check_switcher": False,
    # Back to the VitePress manual that hosts this API reference under /api/.
    "external_links": [{"name": "Manual", "url": os.getenv("MANUAL_URL", "https://rainbowrobotics.github.io/rby1-dev/")}],
    "footer_start": ["copyright"],
    "footer_end": ["sphinx-version", "theme-version"],
}
# No section sidebar on the landing page: the cards there are the navigation.
html_sidebars = {"index": []}

html_context = {
    "sdk_version": SDK_VERSION,
    # "Edit on GitHub" points to the documentation source.
    "github_user": "RainbowRobotics",
    "github_repo": "rby1-dev",
    "github_version": os.getenv("DOCS_SOURCE_BRANCH", "dev"),
    "doc_path": "doc/source",
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