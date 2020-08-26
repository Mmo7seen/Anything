#!/usr/bin/env python3
from socket import socket , AF_INET , SOCK_STREAM
s = socket(AF_INET,SOCK_STREAM)
s.bind(("127.0.0.1",4444))
s.listen(1)
c,a = s.accept()
print ("connection from {0}".format(a[0]))
while True:
    data = c.recv(1024).decode("utf-8")
    print(data)
    data_send = str(input("<shell >"))
    data_send = data_send.encode("utf-8")
    c.send(data_send)
