variable "google_region" {
  description = "Google region"
  type        = string
}

variable "ml_server_repository" {
  description = "Docker repository name for the ml server"
  type        = string
}

variable "google_project_id" {
  description = "Google Cloud project ID"
  type        = string
}

variable "google_service_account_email" {
  description = "Service account email for Google Cloud"
  type        = string
}
