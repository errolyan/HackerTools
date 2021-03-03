# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  ftp_default_pages
   Description :  在 FTP 服务器上寻找 WEB 页面
   Envs        :  python == 3.55
                  pip install  
   Date        :  2021/3/2  下午2:04
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


def return_default(ftp):
    try:
        dir_list = ftp.nlst()
    except Exception as e:
        print('[-] Could not list directory contents.\n'
              '[-] Skipping To Next Target.\n'
              '[-] Exception: {}'.format(e))
        return

    ret_list = []
    for file in dir_list:
        fn = file.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print('[+] Found default page: {}'.format(file))
        ret_list.append(file)
    return ret_list


if __name__ == "__main__":
    tgt_host = '192.168.95.179'
    username = 'guest'
    password = 'guest'

    ftp_conn = ftplib.FTP(tgt_host)
    ftp_conn.login(username, password)
    return_default(ftp_conn)
