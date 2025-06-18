#!/usr/bin/env bash

set -e

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <gcloud-config-name> <environment>"
  exit 1
fi

export CLOUDSDK_ACTIVE_CONFIG_NAME=$1

ROOT_DIR=$(cd "$(dirname "$0")"/..; pwd)

cd "$ROOT_DIR/terraform/environments/$2"

terraform init
# terraform destroy \
#   -target=module.lambda.aws_lambda_function.server \
#   -target=google_artifact_registry_repository.tend_attend_ml_repo
OP_VAULT_NAME="Tend Attend" OP_APP_ENV="Production" op run --env-file $ROOT_DIR/terraform/provider.env -- terraform apply
