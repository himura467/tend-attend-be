variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
}

variable "lambda_invoke_arn" {
  description = "Invoke ARN of the Lambda function"
  type        = string
}

variable "api_gateway_timeout" {
  description = "API Gateway timeout in milliseconds"
  type        = number
}

variable "log_retention_in_days" {
  description = "Log retention in days"
  type        = number
}

variable "stage_name" {
  description = "Stage name"
  type        = string
}

variable "domain_name" {
  description = "Domain name"
  type        = string
}

variable "certificate_arn" {
  description = "Certificate ARN for the domain name"
  type        = string
}

variable "api_gateway_throttle_burst_limit" {
  description = "Burst limit for the API Gateway"
  type        = number
}

variable "api_gateway_throttle_rate_limit" {
  description = "Rate limit for the API Gateway"
  type        = number
}

variable "api_gateway_quota_limit" {
  description = "Quota limit for the API Gateway"
  type        = number
}

variable "api_gateway_quota_offset" {
  description = "Quota offset for the API Gateway"
  type        = number
}

variable "api_gateway_quota_period" {
  description = "Quota period for the API Gateway"
  type        = string
}

variable "route53_zone_id" {
  description = "Route 53 zone ID"
  type        = string
}
