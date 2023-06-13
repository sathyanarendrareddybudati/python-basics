from botocore.exceptions import ClientError
from pprint import pprint
from decimal import Decimal
import time
import boto3


client = boto3.client('dynamodb')
def get_movie(title):
    try:
        response = client.get_item(       
                TableName='video_uploader',
                Key={
                        'Keyword': {
                                'S': "{}".format(title),
                        }
                    }
                )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']
    
if __name__ == '__main__':
        ## Get an item from DynamoDB
    movie = get_movie("Subtitle")
    if movie:
       print("Get an item from DynamoDB succeeded............")
       pprint(movie, sort_dicts=False)