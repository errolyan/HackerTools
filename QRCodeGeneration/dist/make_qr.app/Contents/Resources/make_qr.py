# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  make_qr
   Description :  AIM: 
                  Functions: 1. 
                             2. 
   Envs        :  python == 
                  pip install  -i https://pypi.douban.com/simple 
   Author      :  errol
   Date        :  2020/5/13  17:29
   CodeStyle   :  规范,简洁,易懂,可阅读,可维护,可移植!
-------------------------------------------------
   Change Activity:
          2020/5/13 : 新建
-------------------------------------------------
'''


import qrcode
import datetime
import os,getpass


#输入待转换的字符串
qrstr = input("Enter the string to be converted:")
print("Input :"+qrstr)
#采用默认方式生成二维码
qrimg = qrcode.make(qrstr)

#获取当前时间,转化成字符串
timenow = datetime.datetime.now()
timestr = timenow.strftime("%Y-%m-%d-%H-%M-%S")
#生成带时间的二维码图片名,图片保存在桌面上
qrname = "{1}.png".format(getpass.getuser(), timestr)
print("Save as :", qrname)

#保存二维码图片
qrimg.save(qrname)
print("Success!")
