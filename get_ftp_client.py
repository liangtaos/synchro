#!/usr/bin/python
#coding:utf-8

import socket
import time
import sys



def main():
    HOST = ""
    PORT = 1235
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(1)
    c, address = s.accept()
    data = c.recv(10240)
    with open(data) as f:
        for line in f:
	    c.send(line)
 
    



if __name__ == '__main__':
    main()
