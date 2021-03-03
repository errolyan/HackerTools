# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  ftp_anon_login
   Description :  main: 利用ftp登陆主机，查看是否允许匿名登陆
   Envs        :  python == 3.55
                  pip install  ftplib
   Date        :  2021/3/2  下午1:41
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

import ftplib

def anon_login(hostname):
    ftp = ftplib.FTP(hostname)
    try:
        ftp.login('anonymous', 'me@your.com')
        print('\n[*] {} FTP Anonymous Logon Succeeded.'.format(str(hostname)))
        return True
    except Exception as e:
        print('\n[-] {} FTP Anonymous Logon Failed.'.format(str(hostname)))
        print('[-] Exception: {}'.format(e))
        return False
    finally:
        ftp.quit()


if __name__ == "__main__":
    host = '192.168.95.179'
    anon_login(host)

