#!/usr/bin/python
#coding:utf8

import threading
import SocketServer

class ThreadTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        S = self.request
        sock_list.append(S)
        while True:
            self.data = self.request.recv(1024).strip()
            print self.client_address[0]
            print self.data
            id = self.data.split(':')[0]
            print id
            for s in sock_list:
                s.sendall(self.data)
            if not self.data:
                li.remove(S)
                for s in sock_list:
		    s.sendall('%s 退出了聊天室'%id)
                break

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == '__main__':
    sock_list = []
    HOST = ''
    PORT = 9998
    server = ThreadedTCPServer((HOST, PORT), ThreadTCPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    server.serve_forever()
