#!/usr/bin/python
#coding:utf8

from threading import Thread
import Queue
import time
import random




def pro(queue):
    for i in xrange(100):
        queue.put(random.randint(1,10))
        print 'pro put a number',time.ctime()
        #time.sleep(1)


def con(queue):
    time.sleep(2)
    while 1:
	if queue.empty():
	    break
        else:
	    data = queue.get()
            print 'con %s' % data , time.ctime()
                          

if __name__ == '__main__':
    queue = Queue.Queue(10)
    th1 = Thread(target=pro,args=(queue,))
    th1.start()
    th1.join()
    th2 = Thread(target=con,args=(queue,))
    th2.start()
    th2.join()
