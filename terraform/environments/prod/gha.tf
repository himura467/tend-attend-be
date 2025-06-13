module "gha" {
  source                = "../../modules/gha"
  qrcode_server_ecr_arn = module.ecr.qrcode_ecr_repository_arn
}
