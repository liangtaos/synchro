#!/usr/bin/python
#coding:utf-8

import os
import subprocess
import time

def mon_file(file):
    cmd = 'tail -f %s'%(file)
    popen = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pid = popen.pid
    print pid
    while 1:
        line = popen.stdout.readline().strip()
        if line:
            print line

def mon_suprocess(thefile):
    cmd = 'tail -f %s'% thefile
    print cmd
    popen=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    while 1:
	line = popen.stdout.readline().strip()
        if line:
            print line

def mon_y(thefile):
    thefile.seek(0,2)  #把指针移动到最后
    while 1:
	line = thefile.readline()  #按行读,不能使用readlines()或者read()
	if not line:
	    time.sleep(0.1)
            continue
        yield line

#if __name__ == '__main__':
#    f = '/tmp/access_default.log'
#    mon_suprocess(f)

if __name__ == '__main__':
    f = '/tmp/access_default.log'
    mon_file(f)
