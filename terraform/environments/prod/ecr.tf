module "ecr" {
  source                   = "../../modules/ecr"
  qrcode_server_repository = module.op.qrcode_ecr_repository
}
