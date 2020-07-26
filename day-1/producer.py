from kafka import KafkaProducer
from time import sleep
from json import dumps
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
for num in range(333):
    data = {'lucky_number' : num}
    producer.send('demo-topic', value=data)
    sleep(3)