#!/usr/bin/python
#coding:utf-8

import socket
import time
from optparse import OptionParser
import sys

HOST='127.0.0.1'
PORT=1235

parser = OptionParser('usage: %prog [file1] [file2]')
parser.add_option("-o",
		"--options",
		dest="options",
		action="store_true",
		default=False,
		help="options get or put EX: -o get file1 file2",)
def link_server(HOST, PORT, get_file, save_file):
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(get_file)
    while 1:
	data = s.recv(1024)
        if not data: break
        with open(save_file, 'a+') as f:
            f.write(data)
    print '写入完成'
    s.close()

if __name__=='__main__':
    options, args = parser.parse_args()
    print options
    print args
    if not options.options:
	print 'you should input info ,if you do not konw ,you can input -h,thanks'
        sys.exit()
    get_file = args[1]
    save_file = args[2]
    link_server(HOST, PORT, get_file, save_file)
        
	


