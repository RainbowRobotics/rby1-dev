# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from __future__ import annotations
import os
import sys

# -- Environment setup ---------------------------------------------------
# RBY1_DOCS_VERSION
# RBY1_SDK_VERSION

# -- Project information -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "RB-Y1 Hardware & SDK Manual"
copyright = "2025, Rainbow Robotics"
release = os.environ.get("RBY1_DOCS_VERSION", "latest")
author = "Rainbow Robotics"


# -- General configuration -----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    # core
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinx.ext.autosectionlabel",

    # Docstring parser (Napoleon: NumPy/Google 스타일)
    "sphinx.ext.napoleon",

    # Markdown
    "myst_parser",

    # C++ via Doxygen XML
    "breathe",

    # UX
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- MyST parser options -------------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "linkify",
    "tasklist",
    "attrs_block",
]
myst_heading_anchors = 3

# -- Autosummary / Autodoc options ---------------------------------------
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

# -- Intersphinx options -------------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "typing": ("https://docs.python.org/3/library/typing.html", None),
}

# -- HTML/Furo theme options ---------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]
html_css_files = [
    # "numpydoc-tweaks.css",   # optional: see file below
]
html_title = "RB-Y1 Documentation"
html_theme_options = {
    # "announcement": "<em>Important</em> announcement!",
}

# -- Warnings / nitpicky -------------------------------------------------
nitpicky = False
suppress_warnings = ["myst.header", "ref.citation"]

# -- Breathe (C++ from Doxygen XML) --------------------------------------
# Set DOXYGEN_XML env var to the XML folder, else default path
# _breathe_xml = os.environ.get(
#     "DOXYGEN_XML",
#     str(ROOT / "build" / "doxygen" / "xml")
# )
# breathe_projects = {"rby1_cpp": _breathe_xml}
# breathe_default_project = "rby1_cpp"

# -- Copybutton ----------------------------------------------------------
copybutton_prompt_text = r">>> |\.\.\. "
copybutton_prompt_is_regexp = True

# -- Make toctree refs unique across files -------------------------------
autosectionlabel_prefix_document = True

# -- Napoleon options ----------------------------------------------------
napoleon_numpy_docstring = True
napoleon_google_docstring = False
napoleon_preprocess_types = True
napoleon_use_param = True
napoleon_use_rtype = False
napoleon_attr_annotations = True
napoleon_type_aliases = {
    "ndarray": "numpy.ndarray",
    "ArrayLike": "numpy.typing.ArrayLike",
    "Dict": "typing.Dict",
    "List": "typing.List",
    "Tuple": "typing.Tuple",
    "Optional": "typing.Optional",
}

# -- Python Code Block ---------------------------------------------------
pygments_style = 'sphinx'
pygments_dark_style = 'monokai'

# ──────────────────────────────────────────────────────────────────────────────
# Pybind11: make public objects show as rby1_sdk.* (not rby1_sdk._bindings.*)
# ──────────────────────────────────────────────────────────────────────────────
# import importlib

# def _remap_pybind_modules():
#     try:
#         import rby1_sdk
#     except Exception:
#         return

#     def _patch_module_names(mod):
#         for attr, obj in vars(mod).items():
#             m = getattr(obj, "__module__", None)
#             if isinstance(m, str) and m.startswith("rby1_sdk._bindings"):
#                 try:
#                     obj.__module__ = m.replace("rby1_sdk._bindings", "rby1_sdk", 1)
#                 except Exception:
#                     pass

#     # top-level
#     _patch_module_names(rby1_sdk)

#     # 하위 모듈도 가능하면 불러와서 패치
#     for sub in ("math", "upc", "dynamics"):
#         try:
#             smod = importlib.import_module(f"rby1_sdk.{sub}")
#         except Exception:
#             continue
#         _patch_module_names(smod)

# _remap_pybind_modules()



# ──────────────────────────────────────────────────────────────────────────────
# Autodoc: skip private attrs & compiled internals
# ──────────────────────────────────────────────────────────────────────────────
# def skip_member(app, what, name, obj, skip, options):
#     # Hide internal compiled namespaces such as rby1_sdk._bindings.*
#     if name.startswith("_") and not name.startswith("__"):
#         return True
#     mod = getattr(obj, "__module__", "") if obj is not None else ""
#     if isinstance(mod, str) and mod.startswith("rby1_sdk._bindings"):
#         return False  # still show public symbols remapped above
#     return skip


# def setup(app):
#     app.connect("autodoc-skip-member", skip_member)
