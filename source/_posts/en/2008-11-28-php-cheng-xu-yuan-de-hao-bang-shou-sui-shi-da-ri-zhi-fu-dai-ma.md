---
layout: post
lang: en
status: publish
published: true
title: "A PHP Programmer's Best Friend: Instant Logging Utility (with Code)"
author:
  display_name: 小飞熊
  login: fbbear
  email: fbbear@sina.com
  url: 'https://lfbear.com'
author_login: fbbear
author_email: fbbear@sina.com
author_url: 'https://lfbear.com'
wordpress_id: 59
wordpress_url: 'https://lfbear.com/?p=59'
date: '2008-11-28 13:16:37 +0800'
date_gmt: '2008-11-28 05:16:37 +0800'
categories:
  - 程序人生
tags:
  - php
  - 日志类
comments: []
abbrlink: 21965
---
As programmers, one of the most common things we do when debugging is logging—which basically boils down to continuously appending debug information to a text file.

Based on my day-to-day experience, I've noticed that we often need to measure the execution time of certain code blocks while logging. So today, I wrote a logging class that supports execution-time monitoring, and I'd like to share it with everyone. The download link is at the end of the post. Alright, let's start with how to use it:<!--more-->

### Usage

```php
require_once('monitorlogger.class.php'); // Load the class

// Pass the log file name, executing script path, and query string respectively.
// Typically, you only need to change the first parameter. The latter two can be modified if needed, 
// but it is recommended to keep them as is unless you have a specific use case.
$logger = new MonitorLogger('tester.log', $_SERVER['PHP_SELF'], $_SERVER['QUERY_STRING']);

// Logging with timer monitoring
$logger->timeStart(); // Starts the default timer
sleep(2); // Code block being monitored

$logger->timeStart(1); // Starts timer #1
sleep(1); // Code block being monitored

$logger->timeEnd(); // Stops the default timer
$logger->timeGoon(1); // Resume/accumulate timer #1
sleep(3); // Code block being monitored

$logger->timeEnd(1); // Stops timer #1

$logger->log('test log 1234567890'); // Log with default timer info
$logger->log('test log abcdefghij', 1); // Log with timer #1 info

// Normal logging without timers
$logger->log('Your log content goes here');
```

[Download monitorlogger.class.php](/assets/images/20081128_564563.rar)
