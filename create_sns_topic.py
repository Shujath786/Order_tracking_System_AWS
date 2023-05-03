"""
AWS Order Tracking System Project
Create a SNS Topic.
Moh- 2 May 2023

"""

import boto3

#create a sns client

sns = boto3.client('sns')

#create an SNS topic

response = sns.create_topic(Name='OrderShippedNotificationTopic')

#Get the topic ARN(Amazon Resource Name)

topic_arn = response['TopicArn']

print(f"Created SNS Topic with ARN: {topic_arn}")