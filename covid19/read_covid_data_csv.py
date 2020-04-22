import sys
import time
from json import dumps
from kafka import KafkaProducer
from kafka import KafkaAdminClient


def read_csv():
    file = open("C:\\Users\\MEMALKA\\Downloads\\owid-covid-data.csv", "r")
    producer = KafkaProducer(bootstrap_servers=['192.168.56.101:29094'],
                             value_serializer=lambda x:
                             dumps(x).encode('utf-8'))
    clean_topics()

    for line in file:
        print(line)
        producer.send("owid-covid-data", line)
        time.sleep(1)


def clean_topics():
    kafka_admin_client = KafkaAdminClient(bootstrap_servers=['192.168.56.101:29094'])
    topics = kafka_admin_client.list_topics()
    my_topics = []
    for topic in topics:
        if "owid-covid" in topic:
            print(topic)
            my_topics.append(topic)
    kafka_admin_client.delete_topics(my_topics)


read_csv()
