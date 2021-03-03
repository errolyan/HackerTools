# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  tcp_server
   Description :  TCP server
   Envs        :  python == 3.55
                  pip install  
   Date        :  2021/3/3  上午9:50
   CodeStyle   :  规范,简洁,易懂,可阅读,可维护,可移植!
-------------------------------------------------
   Change Activity:
          2021/3/3 : build
-------------------------------------------------
__Author__ = "Yan Errol 13075851954"
__Email__ = "260187357@qq.com"
__Copyright__ = "Copyright 2021, Yan Errol"
-------------------------------------------------
'''


import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print("[*] Listening on %s:%d" % (bind_ip, bind_port))


# this is our client handling thread
def handle_client(client_socket):
    # just print out what the client sends
    request = client_socket.recv(1024)

    print("[*] Received: %s" % request)

    # send back a packet
    client_socket.send(b"ACK!")
    print(client_socket.getpeername())
    client_socket.close()


while True:
    client, addr = server.accept()

    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))

    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
