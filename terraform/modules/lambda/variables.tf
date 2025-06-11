variable "subnet_ids" {
  description = "List of subnet IDs for the Lambda function"
  type        = list(string)
}

variable "security_group_ids" {
  description = "List of security group IDs for the Lambda function"
  type        = list(string)
}

variable "allow_origins" {
  description = "List of allowed origins for CORS"
  type        = list(string)
}

variable "server_lambda_timeout" {
  description = "Timeout for the Server Lambda function in seconds"
  type        = number
}

variable "server_lambda_memory_size" {
  description = "Memory size for the Server Lambda function in MB"
  type        = number
}

variable "cookie_domain" {
  description = "Cookie domain"
  type        = string
}

variable "jwt_secret_key" {
  description = "JWT secret key (openssl rand -hex 32)"
  type        = string
}

variable "aurora_credentials" {
  description = "Credentials for the Aurora database"
  type        = map(string)
}

variable "aws_region" {
  description = "AWS region"
  type        = string
}

variable "db_shard_count" {
  description = "Number of shards for the DB"
  type        = number
}

variable "rds_cluster_instance_url" {
  description = "RDS cluster instance URL"
  type        = string
}

variable "common_dbname" {
  description = "Common DB name"
  type        = string
}

variable "sequence_dbname" {
  description = "Sequence DB name"
  type        = string
}

variable "shard_dbname_prefix" {
  description = "Shard DB name prefix"
  type        = string
}

variable "ml_server_url" {
  description = "URL of the ML server"
  type        = string
}

variable "qrcode_ecr_repository_url" {
  description = "ECR repository URL for the QRCode Lambda function"
  type        = string
}

variable "qrcode_lambda_timeout" {
  description = "Timeout for the QRCode Lambda function in seconds"
  type        = number
}

variable "qrcode_lambda_memory_size" {
  description = "Memory size for the QRCode Lambda function in MB"
  type        = number
}
