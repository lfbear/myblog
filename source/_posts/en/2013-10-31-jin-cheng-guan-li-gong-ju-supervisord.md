---
layout: post
status: publish
published: true
title: "Supervisord: A Powerful Process Management Tool"
lang: en
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
It is no exaggeration to describe it as "powerful." Born in the Python ecosystem, Supervisord has grown into a highly mature process management tool. With just some simple installation and configuration, you can turn any non-daemon process into a daemon. Any little utility scripts you've written can instantly get a fancy service-like upgrade.

As a quick explainer—why do we want to daemonize? Simply put, it elevates your program from the application layer to the service layer (regardless of whether your program natively behaves like a service).

Now, let's get into the good stuff:

<!-- more -->

### 1. Installation

There are two recommended ways:

*   **Method A**: Use `easy_install`, a Python packaging utility that makes downloading, installing, and updating Python packages a breeze. If you already have `easy_install` installed, simply run the following in your terminal:
    ```bash
    easy_install supervisor
    ```
*   **Method B**: If you don't have `easy_install` and don't care to install it, go to http://pypi.python.org/pypi/supervisor to download the package, extract it, and install it manually:
    ```bash
    python setup.py install
    ```

For more installation methods, you can refer to the official docs at [http://supervisord.org/installing.html](http://supervisord.org/installing.html).

### 2. Configuration

Run the following commands in your shell:

```bash
echo_supervisord_conf > /etc/supervisord.conf
mkdir /etc/supervisord.conf.d
cat << EOF >> /etc/supervisord.conf

[include]
files = /etc/supervisord.conf.d/*.conf
EOF
```

If you want to enable the web-based monitoring dashboard, uncomment the following lines (remove the semicolons) in `/etc/supervisord.conf`:

```ini
[inet_http_server]         ; inet (TCP) server disabled by default
port=127.0.0.1:8080        ; (ip_address:port specifier, *:port for all iface)
username=user              ; (default is no username (open server))
password=123               ; (default is no password (open server))
```

### 3. Creating Process Configuration Files

To keep things modular and easy to maintain, all process-specific configurations should be saved in the `/etc/supervisord.conf.d/` directory as `*.conf` files:

```bash
vi /etc/supervisord.conf.d/yourprogram.conf
```

Here is a configuration example:

```ini
[program:yourprogram]
directory = /var/program
command = /var/program/yourprogram
autostart = true
startsecs = 5
user = root
redirect_stderr = true
stdout_logfile = /var/log/supervisord/yourprogram.log
```

For more detailed program settings, refer to the official configuration documentation: [http://supervisord.org/configuration.html#program-x-section-settings](http://supervisord.org/configuration.html#program-x-section-settings)

### 4. Running Supervisord

Simply run the command in your shell as root:

```bash
supervisord
```
