#!/opt/bb/bin/bbpy

import pika
import sys

message = " ".join(sys.argv[1:])

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = conn.channel()

channel.exchange_declare(exchange='erman_testexch',
                         type='fanout')

channel.basic_publish(exchange='erman_testexch',
                      routing_key='',
                      body=message)

print "Sent the message {}".format(message)

conn.close()
