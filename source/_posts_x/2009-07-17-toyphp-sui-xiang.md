---
layout: post
status: private
published: false
title: toyphp随想记录 --- 打造更好的toyphp
author:
  display_name: 小飞熊
  login: fbbear
  email: fbbear@sina.com
  url: 'https://lfbear.com'
author_login: fbbear
author_email: fbbear@sina.com
author_url: 'https://lfbear.com'
wordpress_id: 342
wordpress_url: 'https://lfbear.com/?p=342'
date: '2009-07-17 14:25:28 +0800'
date_gmt: '2009-07-17 06:25:28 +0800'
categories:
  - 程序人生
tags:
  - toyphp
  - 开发框架
comments: []
abbrlink: 8897
---
<p>1.框架内置html控件 用php来写html常用控件 如 函数html_input 就是文本输入框 然后这个函数有参数 id class value等就是input的属性 这样可以把html页分离出来 然后只要引用css 就可以用php直接输出页面 考虑到可能需要缓冲策略 这里使用类似smaty的缓存原理 但操作上应该有所不同 有必要可以测试一下这么做的效率 应该不错 采用此方法是为了让php程序员不去考虑html的书写 并不需为是否符合w3c标准过多的考虑 初步目标 应该可以达到常用表单的创建和提交</p>
<p>2.数据库操作类 尽量使程序员不需考虑数据库的性能 封装sql语句 对常用操作（不仅局限于增删改查）使用优化后的sql语句</p>
