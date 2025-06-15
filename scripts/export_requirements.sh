#!/usr/bin/env bash

set -e

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <project>"
  exit 1
fi

ROOT_DIR=$(cd "$(dirname "$0")"/..; pwd)

echo "Running export for $1"
cd "$ROOT_DIR/$1"
poetry export -f requirements.txt -o requirements.txt --without-hashes
sed -i '' '/^-e file:/d' requirements.txt
mv requirements.txt "$ROOT_DIR/requirements.txt"
