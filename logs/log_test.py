# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  log_test
   Description :  AIM: 
                  Functions: 1. 
                             2. 
   Envs        :  python == 
                  pip install  -i https://pypi.douban.com/simple 
   Author      :  errol
   Date        :  2020/5/13  09:09
   CodeStyle   :  规范,简洁,易懂,可阅读,可维护,可移植!
-------------------------------------------------
   Change Activity:
          2020/5/13 : 新建
-------------------------------------------------
'''
from logging import StreamHandler, basicConfig, DEBUG,INFO, getLogger, Formatter, FileHandler


def setup_logger(log_filename):
    format_str = '%(asctime)s @ %(name)s  %(levelname)s # %(message)s'
    basicConfig(filename=log_filename, level=INFO, format=format_str)
    stream_handler = StreamHandler()
    stream_handler.setFormatter(Formatter(format_str))
    getLogger().addHandler(stream_handler)

# def setup_file_logger(log_filename):
#     format_str = '%(asctime)s @ %(name)s %(levelname)s # %(message)s'
#     basicConfig(filename=log_filename, level=INFO, format=format_str)

if __name__ == '__main__':
    setup_logger("test11.log")
    logger = getLogger("test")
    logger.info("OK")
