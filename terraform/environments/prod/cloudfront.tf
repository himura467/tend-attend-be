module "cloudfront" {
  source                     = "../../modules/cloudfront"
  lambda_function_url_domain = module.lambda.function_url_domain
  origin_keepalive_timeout   = 60
  origin_read_timeout        = 60
  domain_name                = "aws.${var.domain_name}"
  certificate_arn            = module.route53.certificate_arn
  lambda_function_name       = module.lambda.function_name
  route53_zone_id            = module.route53.zone_id
}
