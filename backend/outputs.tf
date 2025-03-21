output "lambda_arn" {
  value = aws_lambda_function.lambda.arn
}

output "api_endpoint" {
  value = aws_api_gateway_rest_api.api.execution_arn
}
