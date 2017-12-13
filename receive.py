#!/usr/bin/env python
import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='gege')

def callback(ch, method, properties, body):

    print(" sex : {} ,age: {}".format(json.loads(body)["sex"],json.loads(body)["age"]))

channel.basic_consume(callback,
                      queue='gege',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()