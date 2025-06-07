output "invoke_arn" {
  description = "Invoke ARN of the Lambda function"
  value       = aws_lambda_function.this.invoke_arn
}

output "function_name" {
  description = "Name of the Lambda function"
  value       = aws_lambda_function.this.function_name
}

output "function_url_domain" {
  description = "Lambda function URL domain"
  value       = replace(replace(aws_lambda_function_url.this.function_url, "https://", ""), "/", "")
}
