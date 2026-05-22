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
  - Developer Life
tags:
  - nginx
  - websocket
comments: []
abbrlink: 23439
lang: en
---

WebSocket gives us a completely different experience compared to traditional HTTP. I've been digging into it a bit lately. How to deploy a WebSocket application and expose it to the public is the main topic of this post. Since I've always had a soft spot for Nginx, I will outline the configurations for setting up WebSockets on Nginx below.

1. First, check your Nginx version using `nginx -v`. If it's below `1.4`, sorry, but you need to update it immediately. Otherwise, native WebSocket support won't work.

2. The basic configuration is actually quite simple. Below is my setup for a chat application. We start by configuring an `upstream`, and then configure the reverse proxy within the specific server `location` block. Another major advantage of Nginx is its powerful reverse proxy capabilities. Since WebSocket apps usually run on non-standard ports (other than 80), using this proxy allows you to seamlessly integrate the app with the rest of your website.

<!--more-->

```nginx
upstream lab_chat {
    server 127.0.0.1:8080; # your websocket app here
}

location ~ /wschat/ {
    proxy_pass  http://test_chat; # Required
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_http_version 1.1; # Required
    proxy_set_header Upgrade $http_upgrade; # Required
    proxy_set_header Connection "upgrade"; # Required
    proxy_send_timeout 1h; # Send timeout. Make sure to configure this as needed, otherwise it defaults to 60s and disconnects.
    proxy_read_timeout 1h; # Read timeout
}
```

3. **References & Advanced Configurations**
* [http://blog.martinfjordvald.com/2013/02/websockets-in-nginx/](http://blog.martinfjordvald.com/2013/02/websockets-in-nginx/)
* [http://siriux.net/2013/06/nginx-and-websockets/](http://siriux.net/2013/06/nginx-and-websockets/)
