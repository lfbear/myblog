#/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time
from urllib import unquote
from pypinyin import lazy_pinyin

def IsChineseChar(uchar):
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    return False


def cb(x):
    a=True
    try:
        x.decode('latin')
    except:
        a=False
    if a:
        return x.replace('-','')
    else:
        return None

files= os.listdir(os.getcwd()) #得到文件夹下的所有文件名称
for file in files: #遍历文件夹
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开

        if file[-5:] == ".html":
            #print(time.ctime(os.path.getmtime(file)))
            print(unquote(file[11:-5]))
            title = unquote(file[11:-5]).decode('utf8')
            last_title = title
            pinyin = lazy_pinyin(title, errors=cb)
            if len(pinyin) > 0:
                last_title = "-".join(pinyin)
            os.rename(file,file[:11]+last_title+'.md')
            print(file[:11]+last_title+'.md')

        if file[:1] == "2":
            #指定时间格式
            format = "%Y-%m-%d %H:%M:%S"

            Modified_time = file[:10] + ' 00:00:00'
            print('Modified_time:',Modified_time)
        
            #创建struct_time对象
            mtime_t = time.mktime(time.strptime(Modified_time, format))
            os.utime(file, (mtime_t,mtime_t))
            #修改访问时间和修改时间
