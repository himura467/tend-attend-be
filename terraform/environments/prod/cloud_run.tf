module "cloud_run" {
  source                       = "../../modules/cloud_run"
  google_project_id            = var.google_project_id
  google_region                = var.google_region
  cloud_run_image_url          = module.gar.container_image_url
  cloud_run_min_instance_count = 0
  cloud_run_max_instance_count = 1
  depends_on                   = [module.gar]
}
