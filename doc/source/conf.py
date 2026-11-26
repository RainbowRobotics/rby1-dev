"""Sphinx configuration: exports the Python and C++ API reference as Markdown.

The web manual is the VitePress site in manual/. Sphinx is used only because the API pages are
generated from the SDK (autodoc for the pybind11 module, breathe for the Doxygen XML of the C++
headers). `manual/scripts/generate_reference.py` runs this with the `markdown` builder and copies
the result into manual/sdk/python and manual/sdk/cpp.
"""
from __future__ import annotations

import datetime
import importlib
import os
import pathlib
import subprocess


def _submodule_sdk_version() -> str:
    """Tag of the rby1-sdk submodule the API reference is generated from (e.g. v0.10.1)."""
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
project = "RB-Y1 API Reference"
author = "Rainbow Robotics"
copyright = f"2024-{datetime.date.today().year}, Rainbow Robotics"
version = SDK_VERSION
release = SDK_VERSION

# ── General configuration ─────────────────────────────────────────────
root_doc = "sdk/index"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "breathe",
    "sphinx_markdown_builder",
]
templates_path = []
# Proto pages are generated here by `make protoc-doc` and converted for the site by
# manual/scripts/generate_reference.py; they are not part of the Sphinx export.
exclude_patterns = ["sdk/protos/**"]

# ── Markdown output (sphinx-markdown-builder) ─────────────────────────
# Anchors keep the in-page links of the summary tables working in VitePress
# (e.g. #rby1_sdk.Robot_A.send_command).
markdown_anchor_sections = True
markdown_anchor_signatures = True

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

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}

# |sdk_version| in .rst pages
rst_epilog = f"""
.. |sdk_version| replace:: {SDK_VERSION}
"""

# ── Breathe (C++ from Doxygen XML) ────────────────────────────────────
ROOT = pathlib.Path(__file__).resolve().parent.parent
_breathe_xml = os.environ.get("DOXYGEN_XML", str(ROOT / "build" / "doxygen" / "xml"))
breathe_projects = {"rby1-sdk": _breathe_xml}
breathe_default_project = "rby1-sdk"
breathe_use_project_refids = True
breathe_domain_by_extension = {"h": "cpp", "hpp": "cpp", "hh": "cpp", "ipp": "cpp", "c": "c", "cc": "cpp", "cpp": "cpp"}


# ── Pybind11 remap ───────────────────────────────────────────────────
def _remap_pybind_modules():
    """Show `rby1_sdk.X` instead of the internal `rby1_sdk._bindings.X` module names."""
    try:
        import rby1_sdk  # noqa: F401
    except Exception:
        return

    def _patch_module_names(mod):
        for obj in vars(mod).values():
            m = getattr(obj, "__module__", None)
            if isinstance(m, str) and m.startswith("rby1_sdk._bindings"):
                try:
                    obj.__module__ = m.replace("rby1_sdk._bindings", "rby1_sdk", 1)
                except Exception:
                    pass

    for sub in ("math", "upc", "dynamics"):
        try:
            _patch_module_names(importlib.import_module(f"rby1_sdk.{sub}"))
        except Exception:
            continue


_remap_pybind_modules()


def _strip_bindings_in_signature(app, what, name, obj, options, signature, return_annotation):
    def rep(s):
        return s.replace("._bindings", "") if s else s

    return rep(signature), rep(return_annotation)


def _strip_bindings_in_docstring(app, what, name, obj, options, lines):
    for i, line in enumerate(lines):
        lines[i] = line.replace("._bindings", "")


def _keep_signature_keywords():
    """sphinx-markdown-builder drops some signature nodes (e.g. the C++ `constexpr` keyword); keep their text."""
    try:
        from sphinx_markdown_builder import translator
    except ImportError:
        return
    for element in ("desc_sig_keyword", "desc_sig_keyword_type", "desc_sig_space", "desc_sig_name",
                    "desc_sig_punctuation", "desc_sig_operator", "desc_sig_literal_number",
                    "desc_sig_literal_string", "desc_sig_literal_char"):
        translator.PREDEFINED_ELEMENTS.setdefault(element, None)  # None: render the node's text


_keep_signature_keywords()


def setup(app):
    app.connect("autodoc-process-signature", _strip_bindings_in_signature)
    app.connect("autodoc-process-docstring", _strip_bindings_in_docstring)
