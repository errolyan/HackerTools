# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  google_sniff
   Description :  Google 嗅探器
   Envs        :  python == 3.55
                  pip install  
   Date        :  2021/3/2  下午4:41
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

import re
import argparse
from scapy.all import Raw
from scapy.all import sniff, conf


def find_google(pkt):
    if pkt.haslayer(Raw):
        payload = pkt.getlayer(Raw).load
        if 'GET' in payload and 'google' in payload:
            r = re.findall(r'(?i)&q=(.*?)&', payload)
            if r:
                search = r[0].split('&')[0]
                search = search.replace('q=', '').replace('+', ' ').\
                    replace('%20', ' ')
                print('[+] Searched For: {}'.format(search))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='python3 google_sniff.py INTERFACE')
    parser.add_argument('iface', type=str, metavar='INTERFACE',
                        help='specify the interface to listen on')
    args = parser.parse_args()
    conf.iface = args.iface

    try:
        print('[*] Starting Google Sniffer.')
        sniff(filter='tcp port 80', prn=find_google)
    except KeyboardInterrupt:
        exit(0)
