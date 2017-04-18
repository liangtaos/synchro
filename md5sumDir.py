#!/usr/bin/python
#coding:utf8

import hashlib
import time
import threading
import os
import Queue

class MyTest(threading.Thread):
    def __init__(self, pathdir, queue):
	threading.Thread.__init__(self)
        self.pathdir = pathdir
        self.queue = queue
	
    def run(self):
	self.procedir()


    def procedir(self):
        for t, d, fi in os.walk(self.pathdir):
	    for f in fi:
		pwd = os.path.join(t,f)
		#print pwd
		self.queue.put(pwd)


class Coun(threading.Thread):
    def __init__(self, queue):
	threading.Thread.__init__(self)
	self.queue = queue

    def run(self):
	self.xiaofei()


    def xiaofei(self):
        while 1:
            try:
	        path = self.queue.get(1,10)
                md5_v = self.md5value(path)
                print '%s ---------> %s'%(path, md5_v)
            except:
	        sys.exit()

    def md5value(self, f):
        md5 = hashlib.md5()
        fd = open(f)
        while 1:
	    data = fd.read(4096)
            if data:
		md5.update(data)
            else:
		break
        md5_v = md5.hexdigest()
        return md5_v
        


if __name__ == '__main__':
    import sys
    path = sys.argv[1].strip()
    queue = Queue.Queue(1000)
    th1 = MyTest(path,queue)
    th2 = Coun(queue)
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print 'Done'
