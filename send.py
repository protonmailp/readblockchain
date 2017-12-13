#!/usr/bin/env python
import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='gege')




for i  in range(100000000):
    body = {"version": 100, "age": i, "sex": "man"}
    channel.basic_publish(exchange='',
                          routing_key='gege',
                          body=json.dumps(body))

print(" [x] Sent 'ok!'")

connection.close()