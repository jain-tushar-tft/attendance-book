import boto3
from django.conf import settings


class DynamoDBClient:
    def __init__(self, table_name):
        self.table_name = table_name
        self.dynamodb = boto3.resource("dynamodb", region_name=settings.AWS_REGION)
        self.table = self.dynamodb.Table(self.table_name)

    def get_item(self, key):
        response = self.table.get_item(Key=key)
        return response.get('Item')

    def put_item(self, item):
        self.table.put_item(Item=item)
        return item

    def delete_item(self, key):
        self.table.delete_item(Key=key)
