#!/opt/bb/bin/bbpy

import kombu
import sys


with kombu.Connection('amqp://dl:dl@dlrabbitdv.bdns.bloomberg.com:5672/%2F') as conn:
    simple_queue = conn.SimpleQueue('erman_test')
    message = str(sys.argv[1])
    simple_queue.put(message)
    print "Sent message {}".format(message)
    simple_queue.close()
