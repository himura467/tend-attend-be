#!/usr/bin/env bash

set -e

ROOT_DIR=$(cd $(dirname $0)/..; pwd)

# Server build
PYTHON_VERSION=$(cat ${ROOT_DIR}/ta-api/.python-version)
rm -f python.zip main.zip dependencies.zip
bash ${ROOT_DIR}/scripts/export-requirements.sh ta-api
docker build -f ${ROOT_DIR}/docker/server/Dockerfile \
  --build-arg PYTHON_VERSION=${PYTHON_VERSION} \
  --platform linux/amd64 \
  --no-cache \
  --provenance=false \
  -t tend-attend-server:latest ${ROOT_DIR} --progress=plain
CONTAINER_ID=$(docker create --platform linux/amd64 tend-attend-server:latest)
docker cp "$CONTAINER_ID":/python ${ROOT_DIR}
docker cp "$CONTAINER_ID":/main.py ${ROOT_DIR}
docker cp "$CONTAINER_ID":/dependencies ${ROOT_DIR}
docker rm -v "$CONTAINER_ID"
zip -r -X python.zip python -x "*/__pycache__/*"
zip -r -X main.zip main.py
cd dependencies && zip -r -X ../dependencies.zip python -x "*/__pycache__/*" && cd ..
rm -rf ${ROOT_DIR}/python ${ROOT_DIR}/main.py ${ROOT_DIR}/dependencies ${ROOT_DIR}/requirements.txt

# ML Server build
docker build -f ${ROOT_DIR}/docker/ml-server/Dockerfile \
  --target development \
  --platform linux/amd64 \
  --no-cache \
  --provenance=false \
  -t tend-attend-ml:latest ${ROOT_DIR} --progress=plain

# QR Code Server build
PNPM_VERSION=$(grep -o '"pnpm@[^"]*"' ${ROOT_DIR}/ta-qrcode/package.json | grep -o '[0-9]*\.[0-9]*\.[0-9]*')
rm -f qrcode.zip qrcode-dependencies.zip
docker build -f ${ROOT_DIR}/docker/qrcode-server/Dockerfile \
  --build-arg PNPM_VERSION=${PNPM_VERSION} \
  --platform linux/amd64 \
  --no-cache \
  --provenance=false \
  -t tend-attend-qrcode:latest ${ROOT_DIR} --progress=plain
QRCODE_CONTAINER_ID=$(docker create --platform linux/amd64 tend-attend-qrcode:latest)
docker cp "$QRCODE_CONTAINER_ID":/var/task/dist ${ROOT_DIR}
docker cp "$QRCODE_CONTAINER_ID":/var/task/node_modules ${ROOT_DIR}/qrcode-node_modules
docker rm -v "$QRCODE_CONTAINER_ID"
zip -r -X qrcode.zip dist/
cd qrcode-node_modules && zip -r -X ../qrcode-dependencies.zip . -x ".cache/*" && cd ..
rm -rf ${ROOT_DIR}/dist ${ROOT_DIR}/qrcode-node_modules
