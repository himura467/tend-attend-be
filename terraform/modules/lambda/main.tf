resource "aws_iam_role" "lambda" {
  name = "lambda-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Effect = "Allow"
        Sid    = ""
      }
    ]
  })
}

resource "aws_iam_role_policy" "lambda_vpc_access" {
  name = "lambda-vpc-access-policy"
  role = aws_iam_role.lambda.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "ec2:CreateNetworkInterface",
          "ec2:DescribeNetworkInterfaces",
          "ec2:DeleteNetworkInterface"
        ]
        Effect   = "Allow"
        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_cloudwatch" {
  role       = aws_iam_role.lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_s3_bucket" "python_layer" {
  bucket = "tend-attend-lambda-python-layer"
}

resource "aws_s3_object" "python_layer" {
  bucket = aws_s3_bucket.python_layer.id
  key    = "python.zip"
  source = "../../../python.zip"
  etag   = filemd5("../../../python.zip")
}

resource "aws_lambda_layer_version" "python_libs" {
  layer_name          = "PythonLibs"
  compatible_runtimes = ["python3.13"]
  s3_bucket           = aws_s3_bucket.python_layer.id
  s3_key              = aws_s3_object.python_layer.key
  source_code_hash    = filebase64sha256("../../../python.zip")
}

resource "aws_lambda_layer_version" "dependencies" {
  layer_name          = "ProjectDependencies"
  compatible_runtimes = ["python3.13"]
  filename            = "../../../dependencies.zip"
  source_code_hash    = filebase64sha256("../../../dependencies.zip")
}

resource "aws_lambda_function" "this" {
  function_name    = "tend-attend-lambda-function"
  role             = aws_iam_role.lambda.arn
  filename         = "../../../main.zip"
  source_code_hash = filebase64sha256("../../../main.zip")
  handler          = "main.lambda_handler"
  runtime          = "python3.13"
  layers           = [aws_lambda_layer_version.python_libs.arn, aws_lambda_layer_version.dependencies.arn]
  timeout          = var.lambda_timeout
  memory_size      = var.lambda_memory_size
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

resource "aws_lambda_function_url" "this" {
  function_name      = aws_lambda_function.this.function_name
  authorization_type = "AWS_IAM"
  cors {
    allow_credentials = true
    allow_headers     = ["accept", "authorization", "content-type", "origin", "referer"]
    allow_methods     = ["*"]
    allow_origins     = var.allow_origins
    expose_headers    = ["date", "keep-alive"]
    max_age           = 86400
  }
}
