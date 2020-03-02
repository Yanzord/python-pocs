import os
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    topic='HELLO_MESSAGES',
)
publisher.create_topic(topic_name)
future = publisher.publish(topic_name, b'Hello world!', spam='eggs')

print(future.result())