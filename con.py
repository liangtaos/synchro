#!/usr/bin/python
#coding:utf8

from threading import Thread
import time

class consumer(Thread):
    def __init__(self, queue):
	Thread.__init__(self)
	self.queue = queue

    def run(self):
	while 1:
	    if self.queue.empty():
		break
	    data = self.queue.get()
	    print data
	    time.sleep(1)



if __name__ == '__main__':
    import random
    import Queue
    queue = Queue.Queue(10)
    for i in xrange(10):
	queue.put(random.randint(1,100))
    for i in range(3):
	c = consumer(queue)
	c.start()
