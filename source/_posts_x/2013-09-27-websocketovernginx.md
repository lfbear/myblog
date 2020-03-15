---
layout: post
status: publish
published: true
title: WebSocket over Nginx
author:
  display_name: 小飞熊
  login: fbbear
  email: fbbear@sina.com
  url: 'https://lfbear.com'
author_login: fbbear
author_email: fbbear@sina.com
author_url: 'https://lfbear.com'
wordpress_id: 460
wordpress_url: 'https://lfbear.com/?p=460'
date: '2013-09-27 16:27:23 +0800'
date_gmt: '2013-09-27 08:27:23 +0800'
categories:
  - 程序人生
tags:
  - ngnix
  - websocket
comments: []
abbrlink: 23439
---
<p>WebSocket让我们体验到了别样的http，最近小研究了一下。如何讲websocket app如何部署，从而开放给用户使用，是这篇文章将要主要描述的内容。本人对Nginx一直很钟情，所以下面将描述一下nginx上的websocket配置。</p>
<p>1.首先，检查你的nginx版本，nginx -v 如果是1.4以下，不好意思，快去update吧，否则是无法顺利支持websocket的。</p>
<p>2.基础配置其实很简单，下面是我的一个chat app的配置，首先配置一个upstream，然后在具体的server localtion中把代理配好就可以了。nginx的另外一个优势就是强大的proxy，websocket app一般都工作在非80端口，用上这个proxy就可以将应用和你的网站融为一体了。<br />
<!-- more -->
<code><br />
upstream lab_chat {<br />
    server 127.0.0.1:8080; # your websocket app here<br />
}</p>
<p>location ~ /wschat/ {<br />
    proxy_pass  http://test_chat;#必须<br />
    proxy_set_header X-Real-IP $remote_addr;<br />
    proxy_set_header Host $host;<br />
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;<br />
    proxy_http_version 1.1;#必须<br />
    proxy_set_header Upgrade $http_upgrade;#必须<br />
    proxy_set_header Connection "upgrade";#必须<br />
    proxy_send_timeout 1h;#send 超时时间 记得一定要按需配置这个 否则默认60s就断开了<br />
    proxy_read_timeout 1h;#read 超时时间<br />
}<br />
</code></p>
<p>3.参考文献&更多高级配置<br />
http://blog.martinfjordvald.com/2013/02/websockets-in-nginx/<br />
http://siriux.net/2013/06/nginx-and-websockets/</p>
