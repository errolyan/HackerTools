# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  utf2gbk
   Description :  AIM: utf-8 转 gbk
                  Functions: 1. 
                             2. 
   Envs        :  python == 
                  pip install  -i https://pypi.douban.com/simple 
   Author      :  errol
   Date        :  2020/5/11  19:05
   CodeStyle   :  规范,简洁,易懂,可阅读,可维护,可移植!
-------------------------------------------------
   Change Activity:
          2020/5/11 : 新建
-------------------------------------------------
'''


def ReadFile(filePath, encoding="utf-8"):
    with codecs.open(filePath, "r", encoding) as f:
        return f.read()


def WriteFile(filePath, u, encoding="gbk"):
    with codecs.open(filePath, "w", encoding) as f:
        f.write(u)


def UTF8_2_GBK(src, dst):
    content = ReadFile(src, encoding="utf-8")
    WriteFile(dst, content, encoding="gbk")


