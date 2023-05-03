"""
AWS Order Tracking System 
Use Lambda to publish our SQS message to the SNS Topic.
Moh - 2 May 2023
"""
import os
import boto3

# Initialize the SNS client
sns = boto3.client('sns')

# Get the SNS Topic ARN from the Lambda environment variables
sns_topic_arn = os.environ['SNS_TOPIC_ARN']

def lambda_handler(event, context):
    # Get the SQS message from the Lambda event
    sqs_message = event['Records'][0]['body']

    # Publish the SQS message to the SNS Topic
    sns.publish(TopicArn=sns_topic_arn, Message=sqs_message)

    return {
    'statusCode': 200,
    'body': 'SQS message forwarded to the SNS Topic.'
    }