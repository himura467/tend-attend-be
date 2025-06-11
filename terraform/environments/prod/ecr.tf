module "ecr" {
  source                   = "../../modules/ecr"
  aws_region               = var.aws_region
  qrcode_server_repository = "tend-attend-qrcode"
}
