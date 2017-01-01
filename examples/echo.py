#!/usr/bin/env python
# coding: utf-8 
#
# Echo TCP/IP server
# test: telnet localhost 20000
#
from SocketServer import BaseRequestHandler, TCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        prompt = "> "
        while True:
            self.request.send(prompt)
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)
            
if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()