#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


for i in range(100000000):
	


	channel.basic_publish(exchange='',
	                      routing_key='hello',
	                      body=str(i))




print(" [x] Sent 'Hello World!'")
connection.close()