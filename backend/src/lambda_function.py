import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitorCounter')

def lambda_handler(event, context):
    # Example of handling a GET request to retrieve data from DynamoDB
    response = table.get_item(Key={'id': event['pathParameters']['id']})
    
    if 'Item' in response:
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Item not found'})
        }
