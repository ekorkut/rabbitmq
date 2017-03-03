#!/opt/bb/bin/bbpy


import kombu
import time

with kombu.Connection('amqp://dl:dl@dlrabbitdv.bdns.bloomberg.com:5672/%2F') as conn:
    while True:
        simple_queue = conn.SimpleQueue('erman_test')
        message = simple_queue.get(block=True)
        print "Received {}".format(message.payload)
        time.sleep(message.payload.count('.'))
        print "Processed {}".format(message.payload)
        message.ack()
        simple_queue.close()
        

