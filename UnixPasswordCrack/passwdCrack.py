# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  passwdCrack
   Description :  main: unix passwd crack
                  Functions: 1. 
                             2. 
   Functions   :
   Envs        :  python == 
                  pip install  
   Date        :  2021/2/26  下午4:14
   CodeStyle   :  规范,简洁,易懂,可阅读,可维护,可移植!
-------------------------------------------------
   Change Activity:
          2021/2/26 : tag
-------------------------------------------------
__Author__ = "Yan Errol 13075851954"
__Email__ = "260187357@qq.com"
__Copyright__ = "Copyright 2021, Yan Errol"
-------------------------------------------------
'''

from crypt import crypt


def test_pass(crypt_pass):
    salt = crypt_pass[:2]
    dict_file = open('dictionary.txt', 'r')

    for word in dict_file.readlines():
        crypt_word = crypt(word.strip('\n'), salt)
        if crypt_word == crypt_pass:
            print('[+] Found Password: {}'.format(word))
            return

    print('[-] Password Not Found.\n')
    return


if __name__ == '__main__':
    pass_file = open('passwords.txt')
    for line in pass_file.readlines():
        if ':' in line:
            user = line.split(':')[0]
            _crypt_pass = line.split(':')[1].strip()
            print('[*] Cracking Password For: {}'.format(user))
            test_pass(_crypt_pass)
