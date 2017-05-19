#!/usr/bin/python
#coding:utf-8

import socket
import time
import threading
import time
def main(s,id):
    while 1:
        #lock.acquire()
        data = raw_input(' :')
        data_id = "[%s] : %s"%(id,data)
        if data:
            s.sendall(data_id)
        else:
	   continue
        time.sleep(2)
    
def rev(s,id):
    while 1:
	rev_data = s.recv(1024)
        print rev_data

if __name__ == '__main__':
    import sys
    id = sys.argv[1]
    lock = threading.Lock()
    HOST = '192.168.131.150'
    PORT = 9998
    sock = socket.socket()
    sock.connect((HOST, PORT))
    print '【欢迎进入涛涛聊天室】'
    th1 = threading.Thread(target=main, args=(sock,id))
    th2 = threading.Thread(target=rev, args=(sock,id))
    th1.start()
