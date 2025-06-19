module "gar" {
  source               = "../../modules/gar"
  google_project_id    = var.google_project_id
  google_region        = var.google_region
  ml_server_repository = module.op.ml_gar_repository
}
