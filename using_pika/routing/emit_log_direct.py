#!/opt/bb/bin/bbpy

import sys
import pika

severity = sys.argv[1] if len(sys.argv) > 1 else "info"

message = " ".join(sys.argv[2:]) or "Hello World"

conn = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = conn.channel()

channel.exchange_declare(exchange="erman_testexch",
                         type="direct")

channel.basic_publish(exchange="erman_testexch",
                      routing_key=severity,
                      body=message)

print " [x] Sent {}:{}".format(severity,message)

conn.close()
