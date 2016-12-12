#!/usr/bin/python
# -*- coding:utf8 -*

""" A minimal TCP/IP client """

import socket

host = "localhost"
port = 12800

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

print("Connection established on port {}".format(port))

msg_to_send = b""
while msg_to_send != b"fin":

    msg_to_send = input("> ")
    # Peut planter si vous tapez des caractères spéciaux
    msg_to_send = msg_to_send.encode()

    # On envoie le message
    sock.send(msg_to_send)
    msg_recu = sock.recv(1024)
    print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents


print("connection closed")

sock.close()


