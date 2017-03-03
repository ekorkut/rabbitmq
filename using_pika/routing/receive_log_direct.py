#!/opt/bb/bin/bbpy

import sys
import pika

severities = sys.argv[1:]

if not severities:
    print >> sys.stderr, "Need at least one input argument for severity"
    sys.exit(1)

conn = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    
channel = conn.channel()

channel.exchange_declare(exchange="erman_testexch",
                         type="direct")

result = channel.queue_declare(exclusive=True)

queue_name = result.method.queue

for sev in severities:
    channel.queue_bind(exchange="erman_testexch",
                       queue=queue_name,
                       routing_key=sev)

print "Waiting for logs. To exit, press CTRL+C"

def callback(ch, method, props, body):
    print " [x] {}:{}".format(method.routing_key, body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
                       
