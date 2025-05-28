module "gar" {
  source                       = "../../modules/gar"
  google_region                = var.google_region
  ml_server_repository         = "tend-attend-ml"
  google_project_id            = var.google_project_id
  google_service_account_email = var.google_service_account_email
}
