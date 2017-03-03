#!/opt/bb/bin/bbpy

import pika
import datetime


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='erman_test')

def callback(ch, method, prop, body):
    n = datetime.datetime.now()
    print "Received the message '{}' at {}".format(body, n)

channel.basic_consume(callback,
                      queue='erman_test',
                      no_ack=True)

channel.start_consuming()



