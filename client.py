#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

#! -*- coding:utf-8 -*-

import socket, time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 8082))

while True:

    sock.send("tangwei".encode("utf-8"))

    print(sock.recv(20).decode("utf-8"))

    time.sleep(5)