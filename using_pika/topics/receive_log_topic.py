#!/opt/bb/bin/bbpy

import sys
import pika

binding_keys = sys.argv[1:]

if not binding_keys:
    print >> sys.stderr, "At least one binding key is required"
    sys.exit(1)

conn = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = conn.channel()

channel.exchange_declare(exchange="erman_exch",
                         type="topic")

result = channel.queue_declare(exclusive=True)

queue_name = result.method.queue

for key in binding_keys:
    channel.queue_bind(exchange="erman_exch",
                       queue=queue_name,
                       routing_key=key)

print " [*] Waiting for logs. Press CTRL+C to exit it"

def callback(ch, method, props, body):
    print "  [x] {}:{}".format(method.routing_key, body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
