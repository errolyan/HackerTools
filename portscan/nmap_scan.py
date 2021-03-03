# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  nmap_scan
   Description :  main: 端口扫描
   Functions   :
   Envs        :  python == 3.55
                  pip install  python3-nmap
   Date        :  2021/3/2  上午10:02
   CodeStyle   :  规范,简洁,易懂,可阅读,可维护,可移植!
-------------------------------------------------
   Change Activity:
          2021/3/2 : tag
-------------------------------------------------
__Author__ = "Yan Errol 13075851954"
__Email__ = "260187357@qq.com"
__Copyright__ = "Copyright 2021, Yan Errol"
-------------------------------------------------
'''

import nmap
import argparse


def nmap_scan(tgt_host, tgt_ports):
    nm_scan = nmap.PortScanner()
    for tgt_port in tgt_ports:
        nm_scan.scan(tgt_host, tgt_port)
        state = nm_scan[tgt_host]['tcp'][int(tgt_port)]['state']
        print('[*] {} tcp/{} {}'.format(tgt_host,tgt_port,state))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='nmap_scan.py TARGET_HOST -p TARGET_PORTS')
    parser.add_argument('host', type=str, metavar='TARGET_HOST',
                        help="specify target host's IP number")
    parser.add_argument('-p', type=str, metavar='TARGET_PORTS',
                        help='specify target port[s] separated by comma '
                             '(no spaces)')
    args = parser.parse_args()

    args.ports = str(args.p).split(',')
    print(args.host, args.ports)
    nmap_scan(args.host, args.ports)

'''
$ python nmap_scan.py 10.1.8.83 -p 22,21,443
'''