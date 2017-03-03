#!/opt/bb/bin/bbpy

import pika


conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = conn.channel()

channel.exchange_declare(exchange='erman_testexch',
                         type='fanout')


result = channel.queue_declare(exclusive=True)

queue_name = result.method.queue

channel.queue_bind(exchange='erman_testexch',
                   queue=queue_name)

print "Waiting for the logs. To exit, press Ctrl+C"

def callback(ch, method, prop, body):
    print "Received {}".format(body)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()




