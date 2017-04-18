#!/usr/bin/python
#coding:utf8

import multiprocessing 
import os
import time


def func():
    print 'process id : %s'%(os.getpid())
    while 1:
	999 * 999

print 'main id: %s'%(os.getpid())
for i in xrange(20):
    t = multiprocessing.Process(target=func, args=())
    t.start()
