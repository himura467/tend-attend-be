module "gha" {
  source                = "../../modules/gha"
  qrcode_server_ecr_arn = module.ecr.qrcode_ecr_repository_arn
  qrcode_lambda_arn     = module.lambda.qrcode_function_arn
}
