output "container_image_url" {
  description = "The URL of the container image in Google Artifact Registry"
  value       = "${var.google_region}-docker.pkg.dev/${var.google_project_id}/${var.ml_server_repository}/${var.ml_server_repository}:latest"
}
