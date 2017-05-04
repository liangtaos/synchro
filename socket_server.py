#!/usr/bin/python
#coding:utf-8


import threading
import SocketServer

class ThreadTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while True:
	    self.data = self.request.recv(1024).strip()
	    print self.client_address[0]
	    print self.data
	    self.request.sendall(self.data.upper())
            if not self.data:
		break

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == '__main__':
    HOST = ''
    PORT = 9999
    server = ThreadedTCPServer((HOST, PORT), ThreadTCPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    server.serve_forever()



