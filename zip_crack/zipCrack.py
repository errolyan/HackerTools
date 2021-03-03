# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  zipCrack
   Description :  main: 
                  Functions: 1. 
                             2. 
   Functions   :
   Envs        :  python == 
                  pip install  
   Date        :  2021/3/2  上午8:57
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
import zipfile
import argparse
from threading import Thread


def extract_file(zfile, password):
    try:
        zfile.extractall(pwd=password.encode('utf-8'))
        print('[+] Found password: {password}\n')
    except RuntimeError:
        pass


def main(zname, dname):
    z_file = zipfile.ZipFile(zname)
    with open(dname) as pass_file:
        for line in pass_file.readlines():
            password = line.strip('\n')
            t = Thread(target=extract_file, args=(z_file, password))
            t.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage='zip_crack.py ZIPFILE DICTFILE')
    parser.add_argument('zipfile', type=str, metavar='ZIPFILE',
                        help='specify zip file')
    parser.add_argument('dictfile', type=str, metavar='DICTFILE',
                        help='specify dictionary file')
    args = parser.parse_args()
    main(args.zipfile, args.dictfile)

