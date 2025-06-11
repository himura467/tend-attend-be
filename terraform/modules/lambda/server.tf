resource "aws_s3_bucket" "server_python_layer" {
  bucket = "tend-attend-lambda-server-python-layer"
}

resource "aws_s3_object" "server_python_layer" {
  bucket = aws_s3_bucket.server_python_layer.id
  key    = "server-python.zip"
  source = "../../../server-python.zip"
  etag   = filemd5("../../../server-python.zip")
}

resource "aws_lambda_layer_version" "server_python_libs" {
  layer_name          = "ServerPythonLibs"
  compatible_runtimes = ["python3.13"]
  s3_bucket           = aws_s3_bucket.server_python_layer.id
  s3_key              = aws_s3_object.server_python_layer.key
  source_code_hash    = filebase64sha256("../../../server-python.zip")
}

resource "aws_lambda_layer_version" "server_dependencies" {
  layer_name          = "ServerDependencies"
  compatible_runtimes = ["python3.13"]
  filename            = "../../../server-dependencies.zip"
  source_code_hash    = filebase64sha256("../../../server-dependencies.zip")
}

resource "aws_lambda_function" "server" {
  function_name    = "tend-attend-server-lambda-function"
  role             = aws_iam_role.lambda.arn
  architectures    = ["x86_64"]
  filename         = "../../../server.zip"
  source_code_hash = filebase64sha256("../../../server.zip")
  handler          = "main.lambda_handler"
  runtime          = "python3.13"
  layers           = [aws_lambda_layer_version.server_python_libs.arn, aws_lambda_layer_version.server_dependencies.arn]
  timeout          = var.server_lambda_timeout
  memory_size      = var.server_lambda_memory_size
  vpc_config {
    subnet_ids         = var.subnet_ids
    security_group_ids = var.security_group_ids
  }
  environment {
    variables = {
      COOKIE_DOMAIN                   = var.cookie_domain
      JWT_SECRET_KEY                  = var.jwt_secret_key
      AWS_SECRETSMANAGER_SECRET_ID    = var.aurora_credentials.secret_id
      AWS_SECRETSMANAGER_REGION       = var.aws_region
      DB_SHARD_COUNT                  = var.db_shard_count
      AWS_RDS_CLUSTER_INSTANCE_URL    = var.rds_cluster_instance_url
      AWS_RDS_CLUSTER_INSTANCE_PORT   = var.aurora_credentials.port
      AWS_RDS_CLUSTER_MASTER_USERNAME = var.aurora_credentials.username
      AWS_RDS_CLUSTER_MASTER_PASSWORD = var.aurora_credentials.password
      AURORA_COMMON_DBNAME            = var.common_dbname
      AURORA_SEQUENCE_DBNAME          = var.sequence_dbname
      AURORA_SHARD_DBNAME_PREFIX      = var.shard_dbname_prefix
      ML_SERVER_URL                   = var.ml_server_url
    }
  }
}

resource "aws_lambda_function_url" "server" {
  function_name      = aws_lambda_function.server.function_name
  authorization_type = "AWS_IAM"
  cors {
    allow_credentials = true
    allow_headers     = ["content-type"]
    allow_methods     = ["*"]
    allow_origins     = var.allow_origins
    expose_headers    = []
    max_age           = 86400
  }
}
