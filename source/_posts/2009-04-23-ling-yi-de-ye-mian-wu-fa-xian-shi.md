---
layout: post
status: publish
published: true
title: 灵异的&ldquo;页面无法显示&rdquo;
author:
  display_name: 小飞熊
  login: fbbear
  email: fbbear@sina.com
  url: 'https://lfbear.com'
author_login: fbbear
author_email: fbbear@sina.com
author_url: 'https://lfbear.com'
wordpress_id: 302
wordpress_url: 'https://lfbear.com/?p=302'
date: '2009-04-23 15:30:45 +0800'
date_gmt: '2009-04-23 07:30:45 +0800'
categories:
  - 工作心语
tags:
  - '404'
comments:
  - id: 166
    author: huochai
    author_email: bupthuochai@gmail.com
    author_url: ''
    date: '2009-04-23 15:40:29 +0800'
    date_gmt: '2009-04-23 07:40:29 +0800'
    content: 常见第一种问题。。。
abbrlink: 50029
---
<p>最近的一个项目出现了灵异的&ldquo;页面无法显示&rdquo;的情况，总结一下可能的原因：</p>
<p>1.编码问题，混乱的编码很有可能造成这种问题，在一些浏览器下没有问题，另外的一些浏览器下就变成了&ldquo;页面无法显示&rdquo;。<!--more--></p>
<p>排查方法：使用更改页面编码的方法，看看是否用其他常用编码（utf8，gb2312等）出现了一些正常字符，如果有则表明编码出现了问题。</p>
<p>2.不该输出的header：有时使用php的header函数的确很方便，比如做转向等，但是不合适的时候做header输出也会坏了事情。</p>
<p>排查方法：使用ob_get_contents看看是不是有header输出，也可以配合ob系列函数对缓冲区做些手脚</p>
<p>3.bom签名，这个问题曾经让我找得快吐血。</p>
<p>排查方法：使用Dreamweaver（重量级）或者emeditor（轻量级）的编辑器打开脚本，&ldquo;另存为&rdquo;的时候就会发现了。也可以使用一些小程序批量查找。</p>
<p>4.该死的gzip等压缩</p>
<p>这个原因产生的效果是相当的灵异，到处排查都没办法定位原因。如果你也感觉现象灵异，不妨把gizp等压缩模块先弄掉，保证webserver输出最纯朴的http协议流，然后再看看吧。</p>
