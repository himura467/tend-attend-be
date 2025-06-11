resource "google_artifact_registry_repository" "ml_server" {
  location               = var.google_region
  repository_id          = var.ml_server_repository
  format                 = "DOCKER"
  cleanup_policy_dry_run = false
  cleanup_policies {
    id     = "keep-minimum-versions"
    action = "KEEP"
    most_recent_versions {
      keep_count = 3
    }
  }
  cleanup_policies {
    id     = "delete-old-versions"
    action = "DELETE"
    condition {
      tag_state  = "ANY"
      older_than = "30d"
    }
  }
}

resource "google_project_service" "artifact_registry_api" {
  project = var.google_project_id
  service = "artifactregistry.googleapis.com"
}

resource "terraform_data" "docker_push" {
  triggers_replace = [timestamp()]
  provisioner "local-exec" {
    command = <<EOF
      echo "Logging in to Artifact Registry..."
      gcloud auth print-access-token --impersonate-service-account ${var.google_service_account_email} | docker login -u oauth2accesstoken --password-stdin ${var.google_region}-docker.pkg.dev

      echo "Tagging ${var.ml_server_repository} image..."
      docker tag ${var.ml_server_repository}:latest ${var.google_region}-docker.pkg.dev/${var.google_project_id}/${var.ml_server_repository}/${var.ml_server_repository}:latest

      echo "Pushing ${var.ml_server_repository} image to Artifact Registry..."
      docker push ${var.google_region}-docker.pkg.dev/${var.google_project_id}/${var.ml_server_repository}/${var.ml_server_repository}:latest
    EOF
  }
  depends_on = [
    google_artifact_registry_repository.ml_server,
    google_project_service.artifact_registry_api,
  ]
}

resource "time_sleep" "wait_for_push" {
  depends_on      = [terraform_data.docker_push]
  create_duration = "30s"
}
