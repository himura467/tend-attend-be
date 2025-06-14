#!/usr/bin/env bash

set -e

if [[ $# -ne 3 ]]; then
  echo "Usage: $0 <aws-profile> <gcloud-config-name> <environment>"
  exit 1
fi

export AWS_PROFILE=$1
export CLOUDSDK_ACTIVE_CONFIG_NAME=$2

ROOT_DIR=$(cd "$(dirname "$0")"/..; pwd)

cd "$ROOT_DIR/terraform/environments/$3"

terraform init
# terraform destroy \
#   -target=module.lambda.aws_lambda_function.server \
#   -target=google_artifact_registry_repository.tend_attend_ml_repo
terraform apply
