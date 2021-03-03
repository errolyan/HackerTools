# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  print_direction
   Description :  使用 Dpkt 解析数据包
   Envs        :  python == 3.55
                  pip install dpkt
   Date        :  2021/3/2  下午3:24
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

import dpkt
import socket


def print_pcap(pcap_file):
    for ts, buf in pcap_file:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print('[+] Src: {} --> Dst: {}'.format(src,dst))
        except Exception as e:
            print('[-] Exception: {}'.format(e.__class__.__name__))
            pass


if __name__ == '__main__':
    with open('geotest.pcap', 'rb') as file:
        pcap = dpkt.pcap.Reader(file)
        print_pcap(pcap)
