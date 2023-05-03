"""
AWS Order Tracking System Project
Create a standard SQS queue.
Moh- 30 Apr 2023
"""
import boto3

# Create a Boto3 client for SQS
sqs = boto3.client('sqs')

# Create an SQS queue
response = sqs.create_queue(QueueName='CustomerOrderNotifications')

# Retrieve the URL of the created queue
queue_url = response['QueueUrl']
print(f"Queue URL: {queue_url}")