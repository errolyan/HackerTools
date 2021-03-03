# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  print_one2one
   Description :  AIM: 
                  Functions: 1. 
                             2. 
   Envs        :  python == 3.6
   Author      :  errol
   Date        :  2020/5/11  16:47
   CodeStyle   :  规范,简洁,易懂,可阅读,可维护,可移植!
-------------------------------------------------
   Change Activity:
          2020/5/11 : 新建
-------------------------------------------------
'''
import sys


import sys,time
def print_one_by_one(text):
    sys.stdout.write("\r " + " " * 60 + "\r") # /r 光标回到行首
    sys.stdout.flush() #把缓冲区全部输出
    #print text
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

print_one_by_one('规范,简洁,易懂,可阅读,可维护,可移植!')


