---
layout: post
status: publish
published: true
title: 写了一段很罪恶的代码
author:
  display_name: 小飞熊
  login: fbbear
  email: fbbear@sina.com
  url: 'https://lfbear.com'
author_login: fbbear
author_email: fbbear@sina.com
author_url: 'https://lfbear.com'
wordpress_id: 62
wordpress_url: 'https://lfbear.com/?p=62'
date: '2008-11-14 10:47:29 +0800'
date_gmt: '2008-11-14 02:47:29 +0800'
categories:
  - 程序人生
tags:
  - php
  - 外挂
comments:
  - id: 242
    author: countmeon
    author_email: countmeon@gmail.com
    author_url: 'http://pzg.me/'
    date: '2009-10-30 14:57:49 +0800'
    date_gmt: '2009-10-30 06:57:49 +0800'
    content: 呵呵  过于专业了
abbrlink: 5337
---
<p>其实作为游戏作者来讲，是很唾弃外挂这个东西的，因为它让游戏失去了乐趣并且让游戏过早的死掉。原本不想这样的，但是我的虎机的确已经没有钱了，所以还是被迫用写了一个。因为熊熊我是老虎机的作者，所以这段代码暂不予完整公布了（ps：大家都来刷老虎机的话估计我又要收到增加防刷的任务咯，为了给自己减少点工作吧，嘿嘿），但是我会教给大家如何来使用php来写网页游戏外挂。<!--more--></p>
<p>其实先从外挂的原理来说，很简单，就是让机器来代替人，完成有规律的操作。所以外挂对于游戏玩家是件很好的东西，对于程序员们来讲只是为了让自己休息一会的东西，呵呵~ (下面是我的外挂程序中的主体部分)<br />
PHP代码<br />
$ch = curl_init();&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br />
curl_setopt($cu,CURLOPT_REFERER,''http://xxx'');&nbsp;&nbsp;<br />
curl_setopt($ch,CURLOPT_URL, ''http://yyy'');&nbsp;&nbsp;&nbsp;<br />
curl_setopt($ch, CURLOPT_POST, 1);&nbsp;&nbsp;<br />
curl_setopt($ch, CURLOPT_POSTFIELDS, $postdata);&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br />
curl_setopt($cu,CURLOPT_COOKIEFILE,$cookiefile);&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br />
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br />
curl_setopt($ch, CURLOPT_HEADER, false);&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br />
curl_setopt($ch, CURLOPT_NOBODY, false);&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br />
$re = curl_exec($ch);&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br />
curl_close($ch);&nbsp;&nbsp;&nbsp;&nbsp;<br />
&nbsp;<br />
言归正传，在php中主要使用curl系列函数来伪装浏览器对指定脚本进行频繁的规律性调用，curl系列函数，是由curl_init开始，中间使用curl_setopt来设置伪装参数，最后使用curl_exec执行调用，并以curl_close结束。整个流程是否简单，随后我会把setopt的具体参数以及说明贴在文章后面的（主要是setopt来做的伪装工作），它可以伪装登录并且几乎伪装真人的任何操作，很强大~<br />
&nbsp;<br />
Web游戏一般都是基于自己和朋友之间的，因此第一步就是获取好友列表，这个操作通常需要firefox配合firebug抓数据来实现，抓出来的数据需要整理一下，用特殊的符号来分隔。ok，现在程序知道你和谁来玩游戏了，下一步，依然用firefox配合firebug来抓真实游戏地址的url，是要提交游戏参数的那个脚本哦（以下简称为游戏主脚本）~ 使用上面程序中的第3行代码来标明url，并且使用第4、5行来发送post数据($postdata=''act=play&amp;money=123&amp;....'' post数据一般是n多参数用&amp;符来连接，这样子来写)，如果是get方式那就更简单了，直接拼出来放在url后面就可以了，第7行是负责把服务器端的信息返回给$re的，这样就可以解析服务器端的返回，来判断下一步应该做什么事情了，注：服务器端返回的结果一般都是经过编码的，常见的有json，xml和序列化数组的编码方式，记得要解码再分析哦~ 大家可能开始疑问第2行和第6行的作用了，呵呵这两行的主要作用是欺骗，第2行是模拟数据提交前的地址，一般游戏主脚本都会验证这个，以判断该提交参数的来源是否合法，而第6行是模拟正式登录用户的cookie（同理，使用上面的脚本加入 curl_setopt($ch, CURLOPT_COOKIEJAR, $cookiefile); 代码来获取cookie），告诉游戏主脚本的确是你在玩游戏。<br />
&nbsp;<br />
整个流程大体就是这样咯，其他就是给上面这段代码加个循环（遍历到所有好友），加个返回值判断和参数调整或者跳转咯。不同的web游戏可能会增加其他的过滤或者判断，建议写外挂代码前先整体玩一遍游戏，并用firebug记录整个游戏流程，然后再开始动手，否则不容易成功哦~<br />
&nbsp;<br />
可能文中有些地方解释的不足，最后欢迎大家和熊熊一起交流技术~ 以下是关于curl_setopt的常用参数（摘自网络，感谢译者）<br />
curl_setopt参数说明<br />
bool curl_setopt (int ch, string option, mixed value)&nbsp;&nbsp;<br />
curl_setopt()函数将为一个CURL会话设置选项。option参数是你想要的设置，value是这个选项给定的值。&nbsp;&nbsp;<br />
下列选项的值将被作为长整形使用(在option参数中指定)：　&nbsp;&nbsp;<br />
CURLOPT_INFILESIZE: 当你上传一个文件到远程站点，这个选项告诉PHP你上传文件的大小。&nbsp;&nbsp;<br />
CURLOPT_VERBOSE: 如果你想CURL报告每一件意外的事情，设置这个选项为一个非零值。&nbsp;&nbsp;<br />
CURLOPT_HEADER: 如果你想把一个头包含在输出中，设置这个选项为一个非零值。&nbsp;&nbsp;<br />
CURLOPT_NOPROGRESS: 如果你不会PHP为CURL传输显示一个进程条，设置这个选项为一个非零值。注意：PHP自动设置这个选项为非零值，你应该仅仅为了调试的目的来改变这个选项。&nbsp;&nbsp;<br />
CURLOPT_NOBODY: 如果你不想在输出中包含body部分，设置这个选项为一个非零值。&nbsp;&nbsp;<br />
CURLOPT_FAILONERROR: 如果你想让PHP在发生错误(HTTP代码返回大于等于300)时，不显示，设置这个选项为一人非零值。默认行为是返回一个正常页，忽略代码。&nbsp;&nbsp;<br />
CURLOPT_UPLOAD: 如果你想让PHP为上传做准备，设置这个选项为一个非零值。&nbsp;&nbsp;<br />
CURLOPT_POST: 如果你想PHP去做一个正规的HTTP POST，设置这个选项为一个非零值。这个POST是普通的 application/x-www-from-urlencoded 类型，多数被HTML表单使用。&nbsp;&nbsp;<br />
CURLOPT_FTPLISTONLY: 设置这个选项为非零值，PHP将列出FTP的目录名列表。&nbsp;&nbsp;<br />
CURLOPT_FTPAPPEND: 设置这个选项为一个非零值，PHP将应用远程文件代替覆盖它。&nbsp;&nbsp;<br />
CURLOPT_NETRC: 设置这个选项为一个非零值，PHP将在你的 ~./netrc 文件中查找你要建立连接的远程站点的用户名及密码。&nbsp;&nbsp;<br />
CURLOPT_FOLLOWLOCATION: 设置这个选项为一个非零值(象 &ldquo;Location: &ldquo;)的头，服务器会把它当做HTTP头的一部分发送(注意这是递归的，PHP将发送形如 &ldquo;Location: &ldquo;的头)。&nbsp;&nbsp;<br />
CURLOPT_PUT: 设置这个选项为一个非零值去用HTTP上传一个文件。要上传这个文件必须设置CURLOPT_INFILE和CURLOPT_INFILESIZE选项.&nbsp;&nbsp;<br />
CURLOPT_MUTE: 设置这个选项为一个非零值，PHP对于CURL函数将完全沉默。&nbsp;&nbsp;<br />
CURLOPT_TIMEOUT: 设置一个长整形数，作为最大延续多少秒。&nbsp;&nbsp;<br />
CURLOPT_LOW_SPEED_LIMIT: 设置一个长整形数，控制传送多少字节。&nbsp;&nbsp;<br />
CURLOPT_LOW_SPEED_TIME: 设置一个长整形数，控制多少秒传送CURLOPT_LOW_SPEED_LIMIT规定的字节数。&nbsp;&nbsp;<br />
CURLOPT_RESUME_FROM: 传递一个包含字节偏移地址的长整形参数，(你想转移到的开始表单)。&nbsp;&nbsp;<br />
CURLOPT_SSLVERSION: 传递一个包含SSL版本的长参数。默认PHP将被它自己努力的确定，在更多的安全中你必须手工设置。&nbsp;&nbsp;<br />
CURLOPT_TIMECONDITION: 传递一个长参数，指定怎么处理CURLOPT_TIMEVALUE参数。你可以设置这个参数为TIMECOND_IFMODSINCE 或 TIMECOND_ISUNMODSINCE。这仅用于HTTP。&nbsp;&nbsp;<br />
CURLOPT_TIMEVALUE: 传递一个从1970-1-1开始到现在的秒数。这个时间将被CURLOPT_TIMEVALUE选项作为指定值使用，或被默认TIMECOND_IFMODSINCE使用。&nbsp;&nbsp;<br />
<span style="color: #999999;">下列选项的值将被作为字符串：　&nbsp;&nbsp;<br />
CURLOPT_URL: 这是你想用PHP取回的URL地址。你也可以在用curl_init()函数初始化时设置这个选项。&nbsp;&nbsp;<br />
CURLOPT_USERPWD: 传递一个形如[username]:[password]风格的字符串,作用PHP去连接。&nbsp;&nbsp;<br />
CURLOPT_PROXYUSERPWD: 传递一个形如[username]:[password] 格式的字符串去连接HTTP代理。&nbsp;&nbsp;<br />
CURLOPT_RANGE: 传递一个你想指定的范围。它应该是&rdquo;X-Y&rdquo;格式，X或Y是被除外的。HTTP传送同样支持几个间隔，用逗句来分隔(X-Y,N-M)。&nbsp;&nbsp;<br />
CURLOPT_POSTFIELDS: 传递一个作为HTTP &ldquo;POST&rdquo;操作的所有数据的字符串。&nbsp;&nbsp;<br />
CURLOPT_REFERER: 在HTTP请求中包含一个&rdquo;referer&rdquo;头的字符串。&nbsp;&nbsp;<br />
CURLOPT_USERAGENT: 在HTTP请求中包含一个&rdquo;user-agent&rdquo;头的字符串。&nbsp;&nbsp;<br />
CURLOPT_FTPPORT: 传递一个包含被ftp &ldquo;POST&rdquo;指令使用的IP地址。这个POST指令告诉远程服务器去连接我们指定的IP地址。这个字符串可以是一个IP地址，一个主机名，一个网络界面名(在UNIX下)，或是&lsquo;-&rsquo;(使用系统默认IP地址)。&nbsp;&nbsp;<br />
CURLOPT_COOKIE: 传递一个包含HTTP cookie的头连接。&nbsp;&nbsp;<br />
CURLOPT_SSLCERT: 传递一个包含PEM格式证书的字符串。&nbsp;&nbsp;<br />
CURLOPT_SSLCERTPASSWD: 传递一个包含使用CURLOPT_SSLCERT证书必需的密码。&nbsp;&nbsp;<br />
CURLOPT_COOKIEFILE: 传递一个包含cookie数据的文件的名字的字符串。这个cookie文件可以是Netscape格式，或是堆存在文件中的HTTP风格的头。&nbsp;&nbsp;<br />
CURLOPT_CUSTOMREQUEST: 当进行HTTP请求时，传递一个字符被GET或HEAD使用。注意: 在确认你的服务器支持命令先不要去这样做。下列的选项要求一个文件描述(通过使用fopen()函数获得)：　&nbsp;&nbsp;<br />
CURLOPT_FILE: 这个文件将是你放置传送的输出文件，默认是STDOUT.&nbsp;&nbsp;<br />
CURLOPT_INFILE: 这个文件是你传送过来的输入文件。&nbsp;&nbsp;<br />
CURLOPT_WRITEHEADER: 这个文件写有你输出的头部分。&nbsp;&nbsp;<br />
CURLOPT_STDERR: 这个文件写有错误而不是stderr。用来获取需要登录的页面的例子,当前做法是每次或许都登录一次,有需要的人再做改进了.&nbsp; </span></p>
