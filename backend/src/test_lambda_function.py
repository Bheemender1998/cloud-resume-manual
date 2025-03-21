import pytest
from unittest.mock import patch
import lambda_function  # import your Lambda function

def test_lambda_handler():
    event = {'pathParameters': {'id': 'visitorCountId'}}
    context = {}
    
    with patch('boto3.resource') as mock_dynamodb:
        mock_table = mock_dynamodb.return_value.Table.return_value
        mock_table.get_item.return_value = {'Item': {'id': 'visitorCountId', 'count': 5}}
        
        response = your_lambda_function.lambda_handler(event, context)
        assert response['statusCode'] == 200
        assert 'count' in response['body']
