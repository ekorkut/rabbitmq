#!/opt/bb/bin/bbpy

import sys
import pika

import time


conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = conn.channel()

channel.queue_declare(queue='erman_test',durable=True)

print "Waiting for messages. To exit press CTRL+C"

def callback(ch, method, prop, body):
    print "Received the message '{}'".format(body)
    time.sleep(body.count('.'))
    print "Done"
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='erman_test')

channel.start_consuming()


    
