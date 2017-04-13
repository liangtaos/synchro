#!/usr/bin/python
#coding:utf-8


import threading
import time

class MyThread(threading.Thread):
    def __init__(self):
	threading.Thread.__init__(self)
	self.setName('new_'+ self.name)

    def run(self):
	print "I am %s "% self.name, time.ctime()




if __name__ == '__main__':
    for i in range(1000000):
	t = MyThread()
	t.start()
        t.join()
    print 'over'
