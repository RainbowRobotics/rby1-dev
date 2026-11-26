# Build of the RB-Y1 web manual: VitePress site in ../manual, API reference generated with Sphinx.

# ------------------------------------------------------------------------------
# Paths
# ------------------------------------------------------------------------------
SOURCEDIR      = source
BUILDDIR       = build

# ------------------------------------------------------------------------------
# SDK version the API reference is generated from
# ------------------------------------------------------------------------------
# Defaults to the tag the SDK submodule is checked out at, so a rebuild never moves the submodule back.
# To document another release: make -C doc html SDK_TAG=v0.11.0, then commit external/rby1-sdk.
SDK_TAG ?= $(shell git -C "$(CURDIR)/../external/rby1-sdk" describe --tags --exact-match 2>/dev/null || echo v0.10.1)

REPO_ROOT        := $(abspath $(CURDIR)/..)
EXTERNAL_SDK_DIR := $(REPO_ROOT)/external/rby1-sdk


# ------------------------------------------------------------------------------
# Python / pip
# ------------------------------------------------------------------------------
PYTHON ?= python3
PIP    ?= $(PYTHON) -m pip


# ------------------------------------------------------------------------------
# protoc-gen-doc (Docker)
# ------------------------------------------------------------------------------
DOCKER        ?= docker
PROTOC_IMAGE  ?= pseudomuto/protoc-gen-doc:latest
PROTO_SRC     ?= $(abspath $(CURDIR)/../external/rby1-sdk/protos)
PROTO_OUT_DIR ?= $(CURDIR)/$(SOURCEDIR)/sdk/protos/generated
PROTO_DOC_NAME ?= protos.md
PROTO_GLOB    ?= rb/api/*.proto

# ------------------------------------------------------------------------------
# Doxygen (C++)
# ------------------------------------------------------------------------------
DOXYFILE        ?= $(CURDIR)/Doxyfile
DOXYGEN_XML_DIR ?= $(CURDIR)/build/doxygen/xml

# ------------------------------------------------------------------------------
# PHONY
# ------------------------------------------------------------------------------
.PHONY: help protoc-doc clean-proto doxygen-doc clean-doxygen \
        html site reference sdk-pin sdk-install clean joint-limits

# ------------------------------------------------------------------------------
# Help
# ------------------------------------------------------------------------------
help:
	@echo "Targets:"
	@echo "  html (= site)      Build the whole site into ../manual/.vitepress/dist"
	@echo "  reference          Generate the API, proto and joint-limit pages into ../manual"
	@echo "  clean              Remove Doxygen outputs and Sphinx caches"
	@echo "  protoc-doc         Regenerate proto docs (run when protos change; not part of html)"
	@echo "  clean-proto       Remove generated proto docs"
	@echo "  doxygen-doc       Generate Doxygen XML"
	@echo "  clean-doxygen     Remove Doxygen outputs"
	@echo
	@echo "Variables:"
	@echo "  SDK_TAG=<tag>             # default: the tag of external/rby1-sdk ($(SDK_TAG))"
	@echo "  PROTO_SRC=...             # Path to rby1-sdk/protos"
	@echo "  PROTO_GLOB=rb/api/*.proto # Which protos to include"

# ------------------------------------------------------------------------------
# Generate proto docs (Docker)
# ------------------------------------------------------------------------------
protoc-doc:
	@mkdir -p "$(PROTO_OUT_DIR)"
	@echo "[protoc-doc] Using PROTO_SRC=$(PROTO_SRC)"
	@echo "[protoc-doc] Writing to $(PROTO_OUT_DIR)/$(PROTO_DOC_NAME)"
	@$(DOCKER) run --rm -u "$$(id -u):$$(id -g)" \
	  -v "$(PROTO_OUT_DIR):/out" \
	  -v "$(PROTO_SRC):/protos" \
	  --entrypoint '' \
	  $(PROTOC_IMAGE) \
	  bash -lc 'shopt -s globstar nullglob; \
	    protoc -I /protos \
	      --doc_out=/out \
	      --doc_opt=markdown,$(PROTO_DOC_NAME) \
	      /protos/$(PROTO_GLOB)'
	@$(PYTHON) scripts/patch_protos_md.py "$(PROTO_OUT_DIR)/$(PROTO_DOC_NAME)"
	@$(PYTHON) scripts/generate_proto_type_pages.py
	@$(PYTHON) scripts/generate_proto_catalog.py
	

clean-proto:
	@echo "[clean-proto] Removing $(PROTO_OUT_DIR)/$(PROTO_DOC_NAME)"
	@rm -f "$(PROTO_OUT_DIR)/$(PROTO_DOC_NAME)"
	@rm -f "$(PROTO_OUT_DIR)/proto_types.rst"
	@rm -rf "$(PROTO_OUT_DIR)/types"

# ------------------------------------------------------------------------------
# Doxygen (C++) via container
# ------------------------------------------------------------------------------
doxygen-doc:
	@echo "[doxygen] Using DOXYFILE=$(DOXYFILE)"
	@echo "[doxygen] Writing to DOXYGEN_XML_DIR=$(DOXYGEN_XML_DIR)"
	@mkdir -p "$(CURDIR)/build/doxygen"
	@$(DOCKER) run --rm -u "$$(id -u):$$(id -g)" \
	  -v "$(CURDIR):/data" \
	  -v "$(CURDIR)/../external:/external" \
	  nakatt/doxygen

clean-doxygen:
	@echo "[doxygen] Removing $(DOXYGEN_XML_DIR)"
	@rm -rf "$(DOXYGEN_XML_DIR)"

# ------------------------------------------------------------------------------
# Joint range/speed tables from the SDK URDF models
# ------------------------------------------------------------------------------
joint-limits:
	@$(PYTHON) scripts/generate_joint_limit_tables.py --sdk "$(EXTERNAL_SDK_DIR)" --out "$(REPO_ROOT)/manual/hardware/generated"

# ------------------------------------------------------------------------------
# SDK 태그 고정 (submodule fetch & checkout)
# ------------------------------------------------------------------------------
sdk-pin:
	@echo "[sdk-pin] Using EXTERNAL_SDK_DIR=$(EXTERNAL_SDK_DIR)"
	@git -C "$(REPO_ROOT)" submodule update --init --recursive external/rby1-sdk
	@git -C "$(EXTERNAL_SDK_DIR)" fetch --tags --prune
	@git -C "$(EXTERNAL_SDK_DIR)" checkout --recurse-submodules "$(SDK_TAG)"
	@echo "[sdk-pin] Checked out $(SDK_TAG)"

# ------------------------------------------------------------------------------
# SDK 설치: 고정된 태그의 PyPI 휠 (태그가 아니면 소스 빌드)
# ------------------------------------------------------------------------------
sdk-install: sdk-pin
	@# The Python API pages come from the released wheel of the pinned tag, so no C++ build is needed.
	@VER=$$(git -C "$(EXTERNAL_SDK_DIR)" describe --tags --exact-match 2>/dev/null | sed 's/^v//'); \
	if [ -n "$$VER" ]; then \
		echo "[sdk-install] pip install rby1-sdk==$$VER"; \
		$(PIP) install "rby1-sdk==$$VER"; \
	else \
		echo "[sdk-install] $(SDK_TAG) is not a release tag; building rby1-sdk from source"; \
		$(PIP) install --no-deps "$(EXTERNAL_SDK_DIR)"; \
	fi

# ------------------------------------------------------------------------------
# Site build
# ------------------------------------------------------------------------------
NPM ?= npm

# protoc-doc is not part of the build: the generated proto pages are committed in
# source/sdk/protos/generated. Run `make protoc-doc` when the SDK protos change.
reference: sdk-pin sdk-install doxygen-doc
	@SDK_VERSION=$(SDK_TAG) $(PYTHON) "$(REPO_ROOT)/manual/scripts/generate_reference.py"

site: reference
	@cd "$(REPO_ROOT)/manual" && $(NPM) ci --no-audit --no-fund && SDK_VERSION=$(SDK_TAG) npx vitepress build
	@echo "[site] $(REPO_ROOT)/manual/.vitepress/dist"

html: site

# ------------------------------------------------------------------------------
# Clean
# ------------------------------------------------------------------------------
clean: clean-doxygen
	@rm -rf "$(BUILDDIR)/doctrees" "$(REPO_ROOT)/manual/.vitepress/cache"
