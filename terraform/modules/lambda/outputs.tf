output "server_invoke_arn" {
  description = "Invoke ARN of the Server Lambda function"
  value       = aws_lambda_function.server.invoke_arn
}

output "server_function_name" {
  description = "Name of the Server Lambda function"
  value       = aws_lambda_function.server.function_name
}

output "server_function_url_domain" {
  description = "Server Lambda function URL domain"
  value       = replace(replace(aws_lambda_function_url.server.function_url, "https://", ""), "/", "")
}

output "qrcode_invoke_arn" {
  description = "Invoke ARN of the QRCode Lambda function"
  value       = aws_lambda_function.qrcode.invoke_arn
}

output "qrcode_function_name" {
  description = "Name of the QRCode Lambda function"
  value       = aws_lambda_function.qrcode.function_name
}

output "qrcode_function_url_domain" {
  description = "QRCode Lambda function URL domain"
  value       = replace(replace(aws_lambda_function_url.qrcode.function_url, "https://", ""), "/", "")
}
