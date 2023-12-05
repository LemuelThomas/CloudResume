import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloudresume-test')

'''
This will get the item from DynamoDB, 
update the DynamoDB item, 
and return a JSON-formatted response
'''
def lambda_handler(event, context):
    try:
        response = table.get_item(Key={'id': '0'})
        
        if 'Item' in response:
            views = float(response['Item']['views'])
            views += 1

            table.put_item(Item={'id': '0', 'views': Decimal(views)})

            return {
                'statusCode': 200,
                'body': json.dumps({'views': views})
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Item not found'})
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
