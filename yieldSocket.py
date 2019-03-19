#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

#! -*- coding:utf-8 -*-

import socket,select,time

from collections import deque

tasks = deque()

readHandle = deque()

writeHandle = deque()

allDict = {}

def serverFunc():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("0.0.0.0", 8082))

    server.listen(10)

    while True:

        yield "server wait read", server

        client, address = server.accept()

        print("获取到客户端连接：", client.fileno())

        clientF = clientFunc(client)

        tasks.append(clientF)


def clientFunc(client):

    while True:

        yield "client wait read", client

        readData = client.recv(20)

        print(readData.decode("utf-8"))

        yield "client wait write", client

        string = "tangweilkang"

        client.sendall(string.encode("utf-8"))

serverF = serverFunc()

tasks.append(serverF)

while True:

    while len(tasks):

        everyTask = tasks.popleft()

        resStr, socketHandle = everyTask.send(None)

        if resStr == "server wait read":

            print(resStr)

            if not socketHandle.fileno() in readHandle: readHandle.append(socketHandle.fileno())

            allDict[socketHandle.fileno()] = everyTask

        if resStr == "client wait read":

            print(resStr)

            if not socketHandle.fileno() in readHandle: readHandle.append(socketHandle.fileno())

            allDict[socketHandle.fileno()] = everyTask

        if resStr == "client wait write":

            print(resStr)

            if not socketHandle.fileno() in writeHandle: writeHandle.append(socketHandle.fileno())

            allDict[socketHandle.fileno()] = everyTask


    reads, writes, _ = select.select(readHandle, writeHandle, [])

    print(reads)

    print(writes)

    for everyT in reads:

        tasks.append(allDict[everyT])

        allDict.pop(everyT)


    for everyT in writes:

        tasks.append(allDict[everyT])

        allDict.pop(everyT)









