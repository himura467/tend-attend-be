variable "google_project_id" {
  description = "Google Cloud project ID"
  type        = string
}

variable "google_region" {
  description = "Google region"
  type        = string
}

variable "cloud_run_image_url" {
  description = "URL of the Docker image to deploy on Google Cloud Run"
  type        = string
}

variable "cloud_run_min_instance_count" {
  description = "Minimum number of instances for Cloud Run service"
  type        = number
}

variable "cloud_run_max_instance_count" {
  description = "Maximum number of instances for Cloud Run service"
  type        = number
}
