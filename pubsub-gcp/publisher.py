import time
import constant
from google.cloud import pubsub_v1

def get_callback(api_future, data, ref):

    def callback(api_future):
        try:
            print(
                "Published message {} now has message ID {}".format(
                    data, api_future.result()
                )
            )
            ref["num_messages"] += 1
        except Exception:
            print(
                "A problem occurred when publishing {}: {}\n".format(
                    data, api_future.exception()
                )
            )
            raise

    return callback


def publish():
    client = pubsub_v1.PublisherClient.from_service_account_json(constant.GCP_SERVICE_ACCOUNT)

    topic_path = client.topic_path(constant.PROJECT_ID, constant.TOPIC_NAME)

    data = b"Hello, World!"
    ref = dict({"num_messages": 0})

    api_future = client.publish(topic_path, data=data)
    api_future.add_done_callback(get_callback(api_future, data, ref))

    while api_future.running():
        time.sleep(0.5)
        print("Published {} message(s).".format(ref["num_messages"]))


if __name__ == "__main__":
    publish()