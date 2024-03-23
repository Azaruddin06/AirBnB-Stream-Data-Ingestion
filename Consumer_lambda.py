import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    print(event)
    timestamp =  datetime.now()
    # configure the S3 bucket
    s3 = boto3.client('s3')
    s3_target_bucket = 'airbnb-booking-records-asgn'
    s3_target_object_key = f"{timestamp}-{'output.json'}"
    body = event[0]['body']
    
    
    if bool (body):
        json_content = json.dumps(event[0]['body'])
        s3.put_object(Bucket=s3_target_bucket, Key=s3_target_object_key, Body=json_content.encode('utf-8'))
    return {
        'statusCode': 200,
        'body': json.dumps("Processed data send to S3 bucket")
    }
