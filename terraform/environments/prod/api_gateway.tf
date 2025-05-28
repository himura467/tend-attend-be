module "api_gateway" {
  source                           = "../../modules/api_gateway"
  lambda_function_name             = module.lambda.function_name
  lambda_invoke_arn                = module.lambda.invoke_arn
  api_gateway_timeout              = 60000
  log_retention_in_days            = 30
  stage_name                       = "prod"
  domain_name                      = "aws.${var.domain_name}"
  certificate_arn                  = module.route53.certificate_arn
  api_gateway_throttle_burst_limit = 5
  api_gateway_throttle_rate_limit  = 10
  api_gateway_quota_limit          = 1000
  api_gateway_quota_offset         = 0
  api_gateway_quota_period         = "DAY"
  route53_zone_id                  = module.route53.zone_id
}
