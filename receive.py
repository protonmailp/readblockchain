#!/usr/bin/env python
import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='gege')

def callback(ch, method, properties, body):
    print(" [x] Received %r" )
    print(json.loads(body)["sex"])

channel.basic_consume(callback,
                      queue='gege',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()