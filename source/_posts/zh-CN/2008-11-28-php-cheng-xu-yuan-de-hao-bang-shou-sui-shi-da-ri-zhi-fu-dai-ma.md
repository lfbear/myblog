---
layout: post
status: publish
published: true
title: php程序员的好帮手-随时打日志(附代码)
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
<p>作为程序员，调试程序的时候经常做的就是打日志了，无非就是向一个文本中不断追加调试信息。</p>
<p>根据平日的经验积累，发现很多时候打日志的时候要对某些代码进行运行时间监测，因此今天写了一个可以监测的日志类，分享给大家。代码在文后，好了，先给大家讲一下使用吧：<!--more--></p>
<p>使用方法：</p>
<p><span style="color: #008000;">require_once(''monitorlogger.class.php'');//载入这个类&nbsp;&nbsp; </span></p>
<p><span style="color: #008000;">$logger = new MonitorLogger(''tester.log'',$_SERVER[''PHP_SELF''],$_SERVER[''QUERY_STRING'']);//分别传入日志文件名称,执行脚本和参数。使用时只需要更改第一个参数即可，后面两个也可以根据需要做变动，但推荐无特殊需要不要改动&nbsp;&nbsp; </span></p>
<p><span style="color: #008000;">//带计时打log&nbsp;&nbsp;<br />
$logger->timeStart();//默认计时器开始&nbsp;&nbsp;<br />
sleep(2);//被监测的程序&nbsp;&nbsp;<br />
$logger->timeStart(1);//1号计时器开始&nbsp;&nbsp;<br />
sleep(1);//被监测的程序&nbsp;&nbsp;<br />
$logger->timeEnd();//默认计时器停止&nbsp;&nbsp;<br />
$logger->timeGoon(1);//1号计时器累加计时&nbsp;&nbsp;<br />
sleep(3);//被监测的程序&nbsp;&nbsp;<br />
$logger->timeEnd(1);//1号计时器停止&nbsp;&nbsp;<br />
$logger->log(''test log 1234567890'');//写默认计时器的log&nbsp;&nbsp;<br />
$logger->log(''test log abcdefghij'',1);//写1号计时器的log&nbsp;&nbsp;<br />
//正常打log&nbsp;&nbsp;<br />
$logger->log(''log的内容在这里'');&nbsp; </span></p>
<p>&nbsp;<a href="/assets/images/20081128_564563.rar" target="_blank">下载 monitorlogger.class.php </a></p>
