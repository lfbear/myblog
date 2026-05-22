---
layout: post
status: publish
published: true
title: The Ghostly "Page Cannot Be Displayed" Error
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
  - Professional Thoughts
tags:
  - '404'
comments:
  - id: 166
    author: huochai
    author_email: bupthuochai@gmail.com
    author_url: ''
    date: '2009-04-23 15:40:29 +0800'
    date_gmt: '2009-04-23 07:40:29 +0800'
    content: The first issue is indeed very common...
abbrlink: 50029
lang: en
---

A recent project encountered a ghostly, bizarre "Page Cannot Be Displayed" issue. Here is a summary of the potential culprits:

1. **Encoding Issues**: Mismatched or corrupt character encoding is a very common cause of this issue. A page might load perfectly fine in some browsers, yet throw a "Page Cannot Be Displayed" error in others.

<!--more-->

*Troubleshooting method*: Try manually changing the page encoding in your browser to see if switching to other common encodings (such as UTF-8, GB2312, etc.) renders normal characters. If it does, encoding is definitely your problem.

2. **Unexpected Header Outputs**: While PHP's `header()` function is incredibly convenient for redirects and similar tasks, outputting headers at the wrong time or in an incorrect sequence can break things completely.

*Troubleshooting method*: Use `ob_get_contents()` to inspect whether any content is being outputted before your headers. You can also utilize the `ob_*` series of output buffering functions to manipulate the buffer.

3. **UTF-8 BOM Signatures**: This one has driven me to the brink of coughing up blood in the past.

*Troubleshooting method*: Open the script file in an editor like Dreamweaver (heavyweight) or EmEditor (lightweight). When you click "Save As", you'll be able to see if the BOM signature option is enabled. Alternatively, you can use a small script to scan your codebase in batches.

4. **Accursed Gzip (or similar) Compression**

The symptoms caused by this are exceptionally weird, making it nearly impossible to pinpoint through standard debugging. If you are experiencing a similarly ghostly issue, try disabling Gzip or other compression modules entirely. Force your web server to output the rawest, most primitive HTTP protocol stream, and then see what happens.
