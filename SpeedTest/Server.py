#!/usr/bin/python3

import sys, time
from socket import *
import threading

BUFSIZE = 1024000
port = 5000
def server():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('10.30.200.126', int(port)))
    s.listen()
    print ('Server ready...')
    while 1:
        conn, (host, remoteport) = s.accept()
        while 1:
            data = conn.recv(BUFSIZE)
            if not data:
                break
            del data
        #conn.send('OK\n')
        conn.close()
        print ('Done with', host, 'port', remoteport)
server()