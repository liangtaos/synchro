#!/usr/bin/python
#coding:utf-8

from subprocess import Popen, PIPE
import sys
import os


class A(object):
    def __init__(self, cmd):
	self.cmd = cmd

    def process(self):
	p = Popen('%s'%self.cmd,shell=True,stdout=PIPE)
	data_cmd = p.stdout.read()
        return data_cmd

	




def main():
    cmd = sys.argv[1]
    a = A(cmd)
    data_cmd = a.process()
    #print data_cmd
    data = data_cmd.split('\n')
    for li in data:
        if '127.0.0.1' in li:
	    continue
	if 'inet addr' in li:
	    d = li.split()[1].split(':')[-1]
            print d

if __name__ == '__main__':
    main()
