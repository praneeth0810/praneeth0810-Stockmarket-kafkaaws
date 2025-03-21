import pandas as pd
from kafka import KafkaConsumer, KafkaProducer
from time import sleep
from json import dumps,loads
import json
from s3fs import S3FileSystem

consumer = KafkaConsumer(
    'demo_test',
    bootstrap_servers=['18.226.170.164:9092'],
    value_deserializer = lambda x: loads(x.decode('utf-8'))
)

s3 = S3FileSystem()
for count,i in enumerate(consumer):
    with s3.open("s3://kafka-stock-market-data-pranchav/stock_market{}.json".format(count),'w') as file:
        json.dump(i.value,file)  
