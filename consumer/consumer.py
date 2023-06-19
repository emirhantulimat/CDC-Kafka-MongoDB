from kafka import KafkaConsumer
import os

kafka_bootstrap_servers = os.environ['KAFKA_BROKERCONNECT']
kafka_topic = 'X'
kafka_group_id = 'group'+os.environ['CONSUMER_ID']

consumer = KafkaConsumer(kafka_topic, bootstrap_servers=kafka_bootstrap_servers, group_id=kafka_group_id)

for message in consumer:
    msg = message.value.decode('utf-8')
    print('Consumer['+os.environ['CONSUMER_ID'] +
          '] ---------------->', msg)

consumer.close()