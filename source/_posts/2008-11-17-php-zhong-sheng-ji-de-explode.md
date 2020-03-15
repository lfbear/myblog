---
layout: post
status: publish
published: true
title: php中升级的explode
author:
  display_name: 小飞熊
  login: fbbear
  email: fbbear@sina.com
  url: 'https://lfbear.com'
author_login: fbbear
author_email: fbbear@sina.com
author_url: 'https://lfbear.com'
wordpress_id: 64
wordpress_url: 'https://lfbear.com/?p=64'
date: '2008-11-17 17:20:11 +0800'
date_gmt: '2008-11-17 09:20:11 +0800'
categories:
  - 程序人生
tags:
  - php
  - tool
  - 小工具
  - explode
comments: []
abbrlink: 49522
---
<p>explode在php中的功能是将字符串按照特定分隔符分开，然后放入数组中。经常使用这个函数的同学可能会发现当字符串中含有不想分隔的分隔符的时候 比如&ldquo;name|pass&rdquo; 这样按&ldquo;|&rdquo;分隔是不会存在问题的，但是如果这样&ldquo;myuser|pass|123&rdquo; 这样pass和123也会被分隔开，今天工作的时候遇到了这个问题，因此写了一段代码，来搞定这个。<!--more--></p>
<p>举个例子，现在有字符串 $s = ''myinfo|myname|mypass|12|3|456|789'';<br />
&nbsp;<br />
其中12|3是不想被分开的整体，可以这样来搞定：<br />
&nbsp;<br />
$rs = adv_explode($s,''|'',3,2); 意思是把$s作为要分隔的字符串，分隔符是|，前面保留3个，后面保留2个进行分隔。呵呵，没有做参数检测，需要的同学可以自己加上哦~代码其实很简单，完全是为了方便大家~<br />
<span style="color: #008000;">PHP代码<br />
/**<br />
&nbsp; * adv_explode 按要求对字符串进行分隔<br />
&nbsp; *<br />
&nbsp; * 详细描述<br />
&nbsp; * @param string $str 要分隔的字符串<br />
&nbsp; * @param string $split 分隔符<br />
&nbsp; * @param int $a 前端正常分隔的元素个数<br />
&nbsp; * @param int $b 后端正常分隔的元素个数<br />
&nbsp; * @return array<br />
&nbsp; */</span></p>
<p><span style="color: #008000;">function adv_explode($arr,$split,$a,$b)<br />
{<br />
&nbsp;$arr = explode($split,$arr);<br />
&nbsp;$k = 0;<br />
&nbsp;for($i=0;$i<count($arr);$i++)<br />
&nbsp;{<br />
&nbsp;&nbsp;if($i<=$a-1)<br />
&nbsp;&nbsp;{<br />
&nbsp;&nbsp;&nbsp;$re[$i] = $arr[$i];<br />
&nbsp;&nbsp;}<br />
&nbsp;&nbsp;else if($i>=count($arr)-$b)<br />
&nbsp;&nbsp;{</span></p>
<p><span style="color: #008000;">&nbsp;&nbsp;&nbsp;$j = $i-(count($arr)-$a-$b-1);<br />
&nbsp;&nbsp;&nbsp;$re[$j] = $arr[$i];<br />
&nbsp;&nbsp;&nbsp;unset($j);<br />
&nbsp;&nbsp;}<br />
&nbsp;&nbsp;else<br />
&nbsp;&nbsp;{<br />
&nbsp;&nbsp;&nbsp;$tmp[$k] = $arr[$i];<br />
&nbsp;&nbsp;&nbsp;$k++;<br />
&nbsp;&nbsp;}<br />
&nbsp;}<br />
&nbsp;if($k>1)<br />
&nbsp;{<br />
&nbsp;&nbsp;$re[$a] = implode($split,$tmp);<br />
&nbsp;}<br />
&nbsp;else<br />
&nbsp;{<br />
&nbsp;&nbsp;$re[$a] = $tmp[0];<br />
&nbsp;}<br />
&nbsp;return $re;<br />
}</span></p>
