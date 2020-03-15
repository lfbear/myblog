---
layout: post
status: publish
published: true
title: 进程管理工具 Supervisord
author:
  display_name: 小飞熊
  login: fbbear
  email: fbbear@sina.com
  url: 'https://lfbear.com'
author_login: fbbear
author_email: fbbear@sina.com
author_url: 'https://lfbear.com'
wordpress_id: 465
wordpress_url: 'https://lfbear.com/?p=465'
date: '2013-10-31 16:40:47 +0800'
date_gmt: '2013-10-31 08:40:47 +0800'
categories:
  - 程序人生
tags:
  - daem
  - supervisord
comments: []
abbrlink: 48524
---
<p>用强大来形容他一点都不为过，该工具源起python。目前已经成为一款很成熟的进程管理工具。通过简单的安装配置，就可以将你的非daemon进程转成daemon进程。比如自己的写的各种小程序，都可以瞬间华丽变身。<br />
这里科普一下，为啥要转成daemon？简单的说，就是把你的程序从应用层面提升到服务层面（不管你的程序是否具有服务的层次）<br />
下面进入正题：</p>
<!-- more -->
<p>1.安装<br />
一种推荐的方法a)是使用easy_install，一种python的安装工具，可以方便的下载，安装，更新Python packages。<br />
如果已经安装easy_install 只要在shell中输入 easy_install supervisor<br />
b)如果木有，也不想使用easy_install，那就去http://pypi.python.org/pypi/supervisor下载，然后解包python setup.py install吧<br />
更多安装方法也可以参照 http://supervisord.org/installing.html</p>
<p>2.配置<br />
以下命令请在shell运行</p>
<p>echo_supervisord_conf > /etc/supervisord.conf<br />
mkdir /etc/supervisord.conf.d<br />
cat << EOF >> /etc/supervisord.conf.d<br />
[include]<br />
files = /etc/supervisord.conf.d/*.conf<br />
EOF</p>
<p>如果需要打开web监控，请将如下配置前的分号去掉<br />
[inet_http_server]         ; inet (TCP) server disabled by default<br />
port=127.0.0.1:8080        ; (ip_address:port specifier, *:port for all iface)<br />
username=user              ; (default is no username (open server))<br />
password=123               ; (default is no password (open server))</p>
<p>3.给进程建立配置文件<br />
为了方便配置的维护，所有进程配置请保存在/etc/supervisord.conf.d/路径下，以*.conf形式</p>
<p>vi /etc/supervisord.conf.d/yourprogram.conf</p>
<p>配置例子如下<br />
[program:yourprogram]<br />
directory = /var/program<br />
command = /var/program/yourprogram<br />
autostart = true<br />
startsecs = 5<br />
user = root<br />
redirect_stderr = true<br />
stdout_logfile = /var/log/supervisord/yourprogram.log</p>
<p>详细配置请参加官方文档 http://supervisord.org/configuration.html#program-x-section-settings</p>
<p>4.启动<br />
以root身份 在shell中输入 supervisord 即可。</p>
