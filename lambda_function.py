"""
AWS Order Tracking System 
Use Lambda to send a message to the SQS queue, containing the current time.
Moh- 30 Apr 2023
"""
import boto3
import os
from datetime import datetime

def lambda_handler(event, context):
    # Retrieve the queue URL from the environment variable
    queue_url = os.environ['QUEUE_URL']
    
    # Create an SQS client
    sqs = boto3.client('sqs')
    
    # Get the current time in a readable format and send it as a message to the queue
    current_time = datetime.utcnow().isoformat()
    response = sqs.send_message(QueueUrl=queue_url,MessageBody=current_time)
    
    return {
        'statusCode': 200,
        'body': f"Message sent with ID {response['MessageId']}"
    }