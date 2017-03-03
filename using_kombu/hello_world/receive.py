#!/opt/bb/bin/bbpy

import kombu
import datetime

while True:
    with kombu.Connection('amqp://dl:dl@dlrabbitdv.bdns.bloomberg.com:5672/%2F') as conn:
        simple_queue = conn.SimpleQueue('erman_test')
        message = simple_queue.get(block=True)
        print "Received {}".format(message.payload)
        message.ack()
        simple_queue.close()

    
