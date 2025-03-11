import pandas as pd
from kafka import KafkaConsumer, KafkaProducer
from time import sleep
from json import dumps,loads
import json
# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['18.226.170.164:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')  # JSON serialization
)


df = pd.read_csv('data/indexProcessed.csv')
while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    future = producer.send('demo_test', value=dict_stock)
    sleep(1)


producer.flush()