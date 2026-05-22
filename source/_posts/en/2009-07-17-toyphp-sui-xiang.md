---
layout: post
status: private
published: false
title: "Random Thoughts on ToyPHP: Building a Better ToyPHP"
lang: en
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
1. **Built-in HTML Controls in the Framework**: Writing common HTML controls directly in PHP. For instance, an `html_input()` function would generate a text input box, accepting parameters like `id`, `class`, and `value` as element attributes. This allows the layout to be separated from raw HTML, letting PHP render the page directly as long as the CSS is properly referenced. Considering we might need a caching strategy, I could implement something similar to Smarty's caching mechanism, albeit with different operation logic. I should benchmark the efficiency of this approach—it should be pretty good. The goal is to free PHP developers from having to worry about writing HTML or constantly checking for W3C compliance. The initial target is to handle the creation and submission of typical forms.

2. **Database Operations Wrapper**: Making sure developers don't have to stress over database performance. I want to encapsulate SQL queries and use highly optimized queries for common operations (not just limited to standard CRUD).
