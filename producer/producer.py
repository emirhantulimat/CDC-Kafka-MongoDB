import os
from kafka import KafkaProducer
from pymongo import MongoClient
from time import sleep
import socket


kafka_bootstrap_servers = os.environ['KAFKA_BROKERCONNECT']
kafka_topic = 'X'

producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers)

last_count = 0 
count = 0

while(1):
    client = MongoClient('mongodb://mongo:27017/')
    db = client["mydatabase"]
    collection = db["mycollection"]
    cursor = collection.find({}, {"_id": 0, "key": 1, "value": 1}).skip(last_count)
    count = collection.count_documents({}) - last_count
    for change in cursor:
        message = str(change)  # Convert the document to string format
        producer.send(kafka_topic, value=message.encode('utf-8'))
        producer.flush()
        print("Mesaj Gönderildi:", change)
        last_document = change

    last_count += count
    
    client.close()   
    sleep(10)
    

producer.close()

