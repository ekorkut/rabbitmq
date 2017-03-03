#!/opt/bb/bin/bbpy

import sys
import pika


message = ''.join(sys.argv[1:]) or "Hello World!"

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = conn.channel()

channel.queue_declare(queue='erman_test',durable=True)

channel.basic_publish(exchange='',
                      routing_key='erman_test',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2
                      ))

print "Sent the message '{}'".format(message)

conn.close()
                      
