#!/usr/bin/python
#coding:utf-8

from threading import Thread
import threading
import time
from Queue import Queue
import random


class pro(Thread):
    def __init__(self, queue):
	Thread.__init__(self)
	self.queue = queue

    def run(self):
	for i in xrange(10):
	    nu = i
	    self.queue.put(nu)
	    print 'pro : %s----> %s 时间 %s'%(threading.currentThread().getName(),nu, time.ctime())


class odd(Thread):
    def __init__(self, queue):
	Thread.__init__(self)
	self.queue = queue

    def run(self):
	while 1:
	    try:
		data = queue.get(1,10)
                if data % 2 == 0:
		    print 'odd:%s----> %s 时间 %s'%(threading.currentThread().getName(),data, time.ctime())
                else:
		    queue.put(data)
                    continue
	    except:
		print '偶数消费完毕！'
		break

class add(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while 1:
            try:
                data = queue.get(1,10)
                if data % 2 != 0:
                    print 'add:%s----> %s 时间 %s'%(threading.currentThread().getName(),data, time.ctime())
                else:
                    queue.put(data)
                    continue
            except:
                print '奇数消费完毕！'
                break







if __name__ == '__main__':
    #queue = Queue.Queue(10)
    queue = Queue(10)
    th1 = pro(queue) 
    th1.start()
    th2 = odd(queue)
    th2.start()
    th3 = add(queue)
    th3.start()
    th1.join()
    th2.join()
    th3.join()
    print 'over'
