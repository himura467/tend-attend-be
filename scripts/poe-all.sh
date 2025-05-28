#!/usr/bin/env bash

set -e

ROOT_DIR=$(cd $(dirname $0)/..; pwd)

command=$1

projects=(
  "ta-api"
  "ta-cli"
  "ta-core"
  "ta-ml"
)

for project in "${projects[@]}"; do
  echo "Running ${command} for ${project}"
  cd ${ROOT_DIR}/${project}
  
  # For test command, check if test files exist
  if [[ "${command}" = 'test' ]]; then
    test_files=$(find tests -name 'test_*.py' 2>/dev/null | wc -l)
    if [[ ${test_files} -eq 0 ]]; then
      echo "No test files found in ${project}, skipping..."
      continue
    fi
  fi
  
  poetry run poe ${command}
done
