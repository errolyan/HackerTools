# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  录屏
   Description :  AIM: 录屏
                  Functions: 1. mac os 环境搭建
                             2. 录屏代码
   Envs        :  python == 3.6
                  brew install ffmpeg
                  pip install  -i https://pypi.douban.com/simple 
   Author      :  errol
   Date        :  2020/5/11  16:06
   CodeStyle   :  规范,简洁,易懂,可阅读,可维护,可移植!
-------------------------------------------------
   Change Activity:
          2020/5/11 : 新建
-------------------------------------------------
'''

import tkinter as tk
from tkinter.filedialog import askdirectory
import tkinter.messagebox
import subprocess
import time

window = tk.Tk()
window.title('Video Recorder')
window.geometry('300x140')

var_lbl_status = tk.StringVar()
var_lbl_save_path = tk.StringVar()
var_btn_record = tk.StringVar()

on_record = False
save_path = None
child_proc = None
var_lbl_status.set('Recording: OFF')
var_btn_record.set('record')


def get_ffmpeg_cmd(save_path):
    '''
    get video recording command
    '''

    cur_ts = str(int(time.time()))
    filename = '{}.mkv'.format(cur_ts)
    file_path = '{}/{}'.format(save_path, filename)
    # the order in args is important
    # you can speicy your ffmpeg flags here
    args = [
        ['-f', 'avfoundation'],
        ['-framerate', '30'],
        ['-i', '"0"'],
        ['-s', '1280x720'],
        ['-c:v', 'libx264'],
        ['-preset', 'veryfast'],
        ['-crf', '30'],
        ['-c:a', 'copy'],
        ['', file_path],
        ['-async', '1'],
        ['-vsync', '1'],
    ]

    cmd = 'ffmpeg '
    for arg in args:
        cmd += '{} {} '.format(arg[0], arg[1])
    return cmd


def select_path():
    global save_path
    global video_recorder

    path_ = askdirectory()
    save_path = path_


def on_click_record():
    global save_path

    if not save_path:
        tkinter.messagebox.askquestion("save as", "Please click 'save as' to set save path! ")
        return None

    global on_record
    global child_proc

    if not on_record:
        on_record = True
        var_lbl_status.set('Recording: ON')
        var_btn_record.set('stop')

        cmd = get_ffmpeg_cmd(save_path)
        child_proc = subprocess.Popen(cmd, shell=True)
    else:
        on_record = False
        var_lbl_status.set('Recording: OFF')
        var_btn_record.set('record')
        child_proc.terminate()


lbl_status = tk.Label(window,
                      textvariable=var_lbl_status,  # 标签的文字
                      font=('Arial', 15),  # 字体和字体大小
                      width=15, height=2  # 标签长宽
                      )
lbl_status.pack()  # 固定窗口位置

btn_set_save_path = tk.Button(window,
                              text='save as',  # 显示在按钮上的文字
                              width=15, height=2,
                              command=select_path)  # 点击按钮式执行的命令

btn_set_save_path.pack()

lbl_save_path = tk.Label(window,
                         textvariable=var_lbl_save_path,
                         font=('Arial', 15),  # 字体和字体大小
                         width=15, height=2  # 标签长宽
                         )
lbl_status.pack()

btn_start_recrod = tk.Button(window,
                             textvariable=var_btn_record,  # 显示在按钮上的文字
                             width=15, height=2,
                             command=on_click_record)  # 点击按钮式执行的命令

btn_start_recrod.pack()

window.mainloop()


