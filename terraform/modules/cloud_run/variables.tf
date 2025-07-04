variable "google_project_id" {
  description = "Google Cloud project ID"
  type        = string
}

variable "cloud_run_service_name" {
  description = "Name of the Cloud Run service"
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

variable "cloud_run_container_port" {
  description = "Port on which the Cloud Run container listens"
  type        = number
}

variable "cloud_run_min_instance_count" {
  description = "Minimum number of instances for Cloud Run service"
  type        = number
}

variable "cloud_run_max_instance_count" {
  description = "Maximum number of instances for Cloud Run service"
  type        = number
}
