import constant
from google.cloud import pubsub_v1

def subscribe():
    client = pubsub_v1.SubscriberClient.from_service_account_json(constant.GCP_SERVICE_ACCOUNT)

    subscription_path = client.subscription_path(constant.PROJECT_ID, constant.SUBSCRIPTION_NAME)

    def callback(message):
        print(
            "Received message {} of message ID {}\n".format(
                message, message.message_id
            )
        )

        message.ack()
        print("Acknowledged message {}\n".format(message.message_id))

    streaming_pull_future = client.subscribe(
        subscription_path, callback=callback
    )
    print("Listening for messages on {}..\n".format(subscription_path))

    try:
        streaming_pull_future.result()
    except:
        streaming_pull_future.cancel()

if __name__ == "__main__":
    subscribe()