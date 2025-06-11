module "cloudfront" {
  source                     = "../../modules/cloudfront"
  server_function_url_domain = module.lambda.server_function_url_domain
  origin_keepalive_timeout   = 60
  origin_read_timeout        = 60
  domain_name                = "aws.${var.domain_name}"
  certificate_arn            = module.route53.certificate_arn
  server_function_name       = module.lambda.server_function_name
  route53_zone_id            = module.route53.zone_id
}
