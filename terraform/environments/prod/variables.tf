variable "aws_profile" {
  description = "AWS profile"
  type        = string
  default     = "himura"
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "ap-northeast-1"
}

variable "domain_name" {
  description = "Domain name"
  type        = string
  default     = "tend-attend.com"
}
