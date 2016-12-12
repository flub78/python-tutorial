#!/usr/bin/python
# -*- coding:utf8 -*

""" A minimal TCP/IP server 

    test with
    telnet localhost 12800
"""

import socket

host = ''
port = 12800

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
sock.listen(5)

print("server is listening on port {}".format(port))
client_soc, info = sock.accept()

client_soc.send(b"> ")
received_msg = b""
while received_msg != b"quit":

    received_msg = client_soc.recv(1024)
    # L'instruction ci-dessous peut lever une exception si le message
    # Réceptionné comporte des accents

    print(received_msg.decode())
    client_soc.send(b"> ")

print("connection closed")

client_soc.close()
sock.close()

