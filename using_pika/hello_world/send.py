#!/opt/bb/bin/bbpy2.7

import pika
import hostinfo
import datetime


p = pika.URLParameters('ampq://dl:dl@dlrabbitdv.bdns.bloomberg.com:5672/%2F')
conn = pika.BlockingConnection(p)


ch = conn.channel()

ch.queue_declare(queue='erman_test')

ch.basic_publish(exchange='',
                 routing_key='erman_test',
                 body='Hello from {}'.format(hostinfo.localhost().name()))
print "Sent a message at {}".format(datetime.datetime.now())

conn.close()
