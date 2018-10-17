import urllib2
import json
import ssl
import sys
import socket


TCP_IP = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 256

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(3)

    conn, addr = s.accept()
    print 'Connection address:', addr

    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print "received data:", data
        conn.send(data)  # echo
    conn.close()

if __name__ == '__main__':
    main()
