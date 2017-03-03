#!/opt/bb/bin/bbpy

import sys
import pika


routing_key = sys.argv[1] if len(sys.argv) > 1 else "color.animal"

message = sys.argv[2] or "Hello world"

conn = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = conn.channel()

channel.exchange_declare(exchange="erman_exch",
                         type="topic")

channel.basic_publish(exchange="erman_exch",
                      routing_key=routing_key,
                      body=message)

print " [x] Sent {}:{}".format(routing_key, message)

conn.close()

