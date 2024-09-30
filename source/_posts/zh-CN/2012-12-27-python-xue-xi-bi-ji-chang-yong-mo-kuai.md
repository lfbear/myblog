---
layout: post
status: publish
published: true
title: python学习笔记-常用模块
author:
  display_name: 小飞熊
  login: fbbear
  email: fbbear@sina.com
  url: 'https://lfbear.com'
author_login: fbbear
author_email: fbbear@sina.com
author_url: 'https://lfbear.com'
wordpress_id: 427
wordpress_url: 'https://lfbear.com/?p=427'
date: '2012-12-27 14:21:57 +0800'
date_gmt: '2012-12-27 06:21:57 +0800'
categories:
  - 自言自语
tags: []
comments: []
abbrlink: 29589
---
<p>python常用库（官网：http://docs.python.org/release/2.5.2/lib/lib.html）</p>
<!-- more -->
<div>import os // 与操作系统相关的函数：如目录，文件，系统操作system，fork，exec族等等</div>
<div>import sys // 一些系统参数和常见处理函数</div>
<div>import subprocess // 替换os的一些老的开发函数如管道</div>
<div>import multiprocessing // 进程间通信，如进程，消息队列，共享内存</div>
<div>import threading // 线程间通信，如线程，线程队列，线程锁</div>
<div>import thread // 线程间通信另一种创建方式库</div>
<div>import Queue // 消息队列</div>
<div>import time // 时间操作的函数</div>
<div>import signal // 信号处理函数，如signal</div>
<div>import socket // socket通信函数，如socket,accept,gethostname,connect,listen,connect等等</div>
<div>import urllib</div>
<div>import praselib</div>
<div>import smtplib</div>
<div>import xmllib</div>
<div>import telnetlib</div>
<div>...........................</div>
<div>.pyc &nbsp;<wbr />&nbsp;python编译成的二进制跨平台文件，低版本不能加载高版本的该文件，方法：import py_compile</div>
<div>&nbsp;<wbr />&nbsp;&nbsp;<wbr />&nbsp;&nbsp;<wbr />&nbsp;&nbsp;<wbr />&nbsp;&nbsp;<wbr />&nbsp;&nbsp;<wbr />&nbsp;&nbsp;<wbr />&nbsp;&nbsp;<wbr />&nbsp;py_compile.compile("dirpath")或python -m py_compile *.py</div>
<div>存在一个compileall库</div>
<div>.pyo &nbsp;<wbr />&nbsp;python优化编译成的二进制跨平台文件，低版本不能加载高版本，方法：python -O -m py_compile *.py</div>
<div>.pyd &nbsp;<wbr />python的动态链接库</div>
<div>http://www.linuxdiyf.com/bbs/thread-195160-1-6.html</div>
<div></div>
<div>来源&amp;相关：</div>
<div>http://blog.sina.com.cn/s/blog_8ba5fecc0100y8q9.html</div>
<div>http://blog.chinaunix.net/uid-20653538-id-3277663.html</div>
<div></div>
