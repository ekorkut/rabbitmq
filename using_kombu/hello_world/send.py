#!/opt/bb/bin/bbpy

import kombu
import datetime
import hostinfo


with kombu.Connection('amqp://dl:dl@dlrabbitdv.bdns.bloomberg.com:5672/%2F') as conn:
    simple_queue = conn.SimpleQueue('erman_test')
    message = "Hello from {}, using kombu".format(hostinfo.localhost().name())
    simple_queue.put(message)
    print "Sent a message at {}".format(datetime.datetime.now())
    simple_queue.close()
