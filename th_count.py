#!/usr/bin/python
#coding:utf8

from threading import Thread
from time import ctime

class MyThread(Thread):
    def __init__(self):
	Thread.__init__(self)
        #self.num = num

    def run(self):
	global num
	num += 1
	print num,ctime()


if __name__ == "__main__":
    num = 0
    for i in xrange(1000):
	th = MyThread()
        th.start()
        #th.join()

    print 'over'
