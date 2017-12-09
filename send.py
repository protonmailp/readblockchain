#!/usr/bin/env python
import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='gege')


body={"version":100,"age":10,"sex":"man"}


for i  in range(100000000):
    channel.basic_publish(exchange='',
                          routing_key='gege',
                          body=json.dumps(body))

print(" [x] Sent 'Hello World!'")

connection.close()