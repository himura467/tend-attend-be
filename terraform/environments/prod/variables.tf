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

variable "google_project_id" {
  description = "Google Cloud project ID"
  type        = string
  default     = "tend-attend"
}

variable "google_service_account_email" {
  description = "Service account email for Google Cloud"
  type        = string
  default     = "mitarashidango0927@gmail.com"
}

variable "google_region" {
  description = "Google region"
  type        = string
  default     = "asia-northeast1"
}

variable "domain_name" {
  description = "Domain name"
  type        = string
  default     = "tend-attend.com"
}
