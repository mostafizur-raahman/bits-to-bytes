#!/usr/bin/env bash
# Zip BitsToBytes source code for download.
# Excludes: node_modules, .next, .git, build artifacts, dev.log, .env (secrets).
set -e

OUT="/home/z/my-project/download/bits-to-bytes-source.zip"
SRC="/home/z/my-project"

cd "$SRC"

# Clean transient stuff
rm -rf .next dev.log node_modules/.cache 2>/dev/null || true

# Remove old zip if exists
rm -f "$OUT"

# Build exclude list (zip syntax)
EXCLUDES=(
  "node_modules/*"
  "node_modules"
  ".next/*"
  ".next"
  ".git/*"
  ".git"
  "upload/*"
  "upload"
  "skills/*"
  "skills"
  "tsconfig.tsbuildinfo"
  "dev.log"
  ".env"
  "bun.lock"
  "download/*"
  "download"
)

# Build exclude args
EXCLUDE_ARGS=()
for e in "${EXCLUDES[@]}"; do
  EXCLUDE_ARGS+=("-x" "$e")
done

zip -r -q "$OUT" . \
  -x "node_modules/*" \
  -x "node_modules" \
  -x ".next/*" \
  -x ".next" \
  -x ".git/*" \
  -x ".git" \
  -x "upload/*" \
  -x "upload" \
  -x "skills/*" \
  -x "skills" \
  -x "tsconfig.tsbuildinfo" \
  -x "dev.log" \
  -x ".env" \
  -x "bun.lock" \
  -x "download/*" \
  -x "download" \
  -x ".zscripts/*" \
  -x ".zscripts"

ls -lh "$OUT"
echo "---"
echo "Zip contents summary:"
unzip -l "$OUT" | tail -5
