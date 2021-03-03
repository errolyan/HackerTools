# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  截图
   Description :  AIM: 
                  Functions: 1. 
                             2. 
   Envs        :  python == 
                  pip install  -i https://pypi.douban.com/simple 
   Author      :  errol
   Date        :  2020/5/13  17:16
   CodeStyle   :  规范,简洁,易懂,可阅读,可维护,可移植!
-------------------------------------------------
   Change Activity:
          2020/5/13 : 新建
-------------------------------------------------
'''

from PIL import ImageGrab
bbox = (10, 10, 3100,2400 )
# x1: 开始截图的x坐标;x2:开始截图的y坐标;x3:结束截图的x坐标;x4:结束截图的y坐标
im = ImageGrab.grab(bbox)
im.save('as.png')#保存截图文件的路径

