from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='my-cluster-kafka-bootstrap.kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'sample-topic'

for i in range(10):
    message = {'id': i, 'value': random.randint(1, 100)}
    print(f"Sending: {message}")
    producer.send(topic, message)
    time.sleep(1)

producer.flush()
producer.close()

