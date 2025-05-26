resource "google_project_service" "cloud_run_admin_api" {
  project = var.google_project_id
  service = "run.googleapis.com"
}

resource "google_cloud_run_v2_service" "ml_server" {
  name                = "tend-attend-ml-cloud-run"
  location            = var.google_region
  deletion_protection = false
  template {
    containers {
      image = var.cloud_run_image_url
      ports {
        container_port = var.cloud_run_container_port
      }
      startup_probe {
        initial_delay_seconds = 5
        tcp_socket {
          port = var.cloud_run_container_port
        }
      }
      resources {
        limits = {
          cpu    = "1"
          memory = "1024Mi"
        }
      }
    }
    scaling {
      min_instance_count = var.cloud_run_min_instance_count
      max_instance_count = var.cloud_run_max_instance_count
    }
    timeout = 600
  }
  depends_on = [google_project_service.cloud_run_admin_api]
}

data "google_iam_policy" "cloud_run_invoker" {
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}

resource "google_cloud_run_v2_service_iam_policy" "cloud_run_invoker" {
  project     = google_cloud_run_v2_service.ml_server.project
  location    = google_cloud_run_v2_service.ml_server.location
  name        = google_cloud_run_v2_service.ml_server.name
  policy_data = data.google_iam_policy.cloud_run_invoker.policy_data
}
