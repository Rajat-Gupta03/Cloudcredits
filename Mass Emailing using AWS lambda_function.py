import boto3
import json

# Initialize the SES client
ses_client = boto3.client('ses', region_name='ap-south-1')

def lambda_handler(event, context):
    sender_email = "rajatgupta31302@gmail.com"
    recipient_emails = ["rajatrg4083@gmail.com", "rjstyle1234567890@gmail.com"]  # List of recipients
    subject = "AWS Lambda Mass Email Test"
    body_text = "Hello, this is a test email sent using AWS Lambda and SES."
    
    try:
        response = ses_client.send_email(
            Source=sender_email,
            Destination={'ToAddresses': recipient_emails},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': body_text}}
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps(f"Emails sent! Message ID: {response['MessageId']}")
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }
