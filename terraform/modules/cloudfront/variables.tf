variable "server_function_url_domain" {
  description = "Lambda function URL domain for the server"
  type        = string
}

variable "origin_keepalive_timeout" {
  description = "The amount of time, in seconds, that CloudFront waits for a response after forwarding a request to the origin"
  type        = number
  default     = 5
}

variable "origin_read_timeout" {
  description = "The amount of time, in seconds, that CloudFront waits for a response after forwarding a request to the origin"
  type        = number
  default     = 30
}

variable "qrcode_function_url_domain" {
  description = "Lambda function URL domain for the qrcode server"
  type        = string
}

variable "domain_name" {
  description = "Custom domain name for CloudFront distribution"
  type        = string
}

variable "certificate_arn" {
  description = "ACM certificate ARN for SSL/TLS"
  type        = string
}

variable "server_function_name" {
  description = "Lambda function name for the server"
  type        = string
}

variable "qrcode_function_name" {
  description = "Lambda function name for the qrcode server"
  type        = string
}

variable "route53_zone_id" {
  description = "Route53 zone ID"
  type        = string
}
