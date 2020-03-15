#/usr/bin/python
# -*- coding: UTF-8 -*-
# 转换工具
# 将中文命名的post改为拼音命名
# 对修改后的文件进行mtime修复

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

files = os.listdir(os.getcwd())
for file in files:
     if not os.path.isdir(file):
        if file[:1] == "2":
            format = "%Y-%m-%d %H:%M:%S"  #指定时间格式
            modified_time = file[:10] + ' 00:00:00'
            print(file, "modified time:",modified_time)
            mtime_t = time.mktime(time.strptime(modified_time, format))
            os.utime(file, (mtime_t,mtime_t)) #修改访问时间和修改时间

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
