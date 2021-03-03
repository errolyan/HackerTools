# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  port_scan
   Description :  main: 端口扫描
                  Functions: 1. 
                             2. 
   Functions   :
   Envs        :  python == 
                  pip install  
   Date        :  2021/3/2  上午9:35
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

import argparse
import socket
import threading


def port_scan(tgt_host, tgt_ports):
    try:
        tgt_ip = socket.gethostbyname(tgt_host)
    except socket.herror:
        print('[-] Cannot resolve {}: Unknown host'.format(tgt_host))
        return

    try:
        tgt_name = socket.gethostbyaddr(tgt_ip)
        print('\n[+] Scan Results for: {}'.format(tgt_name[0]))
    except socket.herror:
        print('\n[+] Scan Results for: {}'.format(tgt_ip))

    socket.setdefaulttimeout(1)

    for ports in tgt_ports:
        t = threading.Thread(target=conn_scan, args=(tgt_host, int(ports)))
        t.start()


def conn_scan(tgt_host, tgt_port):
    screen_lock = threading.Semaphore()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn_skt:
        try:
            conn_skt.connect((tgt_host, tgt_port))
            conn_skt.send(b'ViolentPython\r\n')
            results = conn_skt.recv(100).decode('utf-8')
            screen_lock.acquire()
            print('[+] {}/tcp open'.format(tgt_port))
            print('   [>] {}'.format(results))
        except OSError:
            screen_lock.acquire()
            print('[-] {}/tcp closed'.format(tgt_port))
        finally:
            screen_lock.release()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='port_scan.py TARGET_HOST -p TARGET_PORTS'
              '\nexample: python3 port_scan.py scanme.nmap.org -p 21,80')

    parser.add_argument('tgt_host', type=str, metavar='TARGET_HOST',
                        help='specify target host (IP address or domain name)')
    parser.add_argument('-p', required=True, type=str, metavar='TARGET_PORTS',
                        help='specify target port[s] separated by comma '
                             '(no spaces)')
    args = parser.parse_args()

    args.tgt_ports = str(args.p).split(',')
    port_scan(args.tgt_host, args.tgt_ports)



'''
$  python3 port_scan.py 10.1.8.83 -p 21,80
'''