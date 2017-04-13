#!/usr/bin/python
#coding:utf-8


import threading
import time

def hello():
    for i in xrange(3):
        print 'hello',time.ctime()


def world():
    for i in xrange(3):
        print 'world'


h_lock = threading.Lock()
w_lock = threading.Lock()
w_lock.acquire()
for i in range(100):
    th1 = threading.Thread(target=hello,args=())
    th1.start()
    th1.join()
print 'over'
