#!/usr/bin/env bash
#
# Build and publish one documentation version with mike.
#
# The docs tooling (docs/, generate_docs.py, mkdocs.yml, docs-requirements.txt) always
# comes from the current checkout (main). This script overlays the message/service
# definitions from an arbitrary ref so every version -- including historical release
# tags that predate the docs tooling -- is rendered with the current generator.
#
# Usage: docs/build_version.sh <ref> <version-label>
#   <ref>           git ref to take msg/ + srv/ from   (e.g. main, 24.R2, 26.R1)
#   <version-label> mike version to publish            (e.g. dev, 24.R2, 26.R1)
set -euo pipefail

REF="${1:?usage: build_version.sh <ref> <version-label>}"
VERSION="${2:?usage: build_version.sh <ref> <version-label>}"

echo "==> Building docs version '${VERSION}' from msg/srv at ref '${REF}'"

# Overlay this ref's definitions cleanly (drop any files that don't exist in REF).
rm -rf msg srv
git checkout "${REF}" -- msg srv

# Regenerate message/service pages and the nav for this exact definition set.
python docs/generate_docs.py

# Publish to the gh-pages branch.
mike deploy --push "${VERSION}"

# Restore main's definitions so the next iteration starts clean.
rm -rf msg srv
git checkout HEAD -- msg srv
