# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  bt_scan
   Description :  搜索蓝牙设备
   Envs        :  python == 3.55
                  pip install  
   Date        :  2021/3/2  下午5:01
   CodeStyle   :  规范,简洁,易懂,可阅读,可维护,可移植!
-------------------------------------------------
   Change Activity:
          2021/3/2 : build
-------------------------------------------------
__Author__ = "Yan Errol 13075851954"
__Email__ = "260187357@qq.com"
__Copyright__ = "Copyright 2021, Yan Errol"
-------------------------------------------------
'''

import time
from bluetooth import *


def find_devs():
    already_found = []
    found_devs = discover_devices(lookup_names=True)
    for addr, name in found_devs:
        if addr not in already_found:
            print('[*] Found Bluetooth Device: {}'.format(str(name)))
            print('[+] MAC Address: {}'.format(str(addr)))
            already_found.append(addr)


if __name__ == '__main__':
    while True:
        try:
            find_devs()
            time.sleep(5)
        except KeyboardInterrupt:
            exit(0)
