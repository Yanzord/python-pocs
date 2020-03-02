import os

GCP_SERVICE_ACCOUNT = '{}/keys/gcp_service_key.json'.format(os.getenv("HOME"))
TOPIC_NAME = 'HELLO_MESSAGES'
SUBSCRIPTION_NAME = 'HELLO_MESSAGES_SUB'
PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT')