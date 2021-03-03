# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  TCP_client
   Description :  TCP 客户端
   Envs        :  python == 3.55
                  pip install  
   Date        :  2021/3/3  上午9:48
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

target_host = "0.0.0.0"
target_port = 9999

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send(b"GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")

# receive data
response = client.recv(4096)

client.close()

print(response)

