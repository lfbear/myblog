---
layout: post
status: publish
published: true
title: 一点点关于angularjs，一点点关于framework
author:
  display_name: 小飞熊
  login: fbbear
  email: fbbear@sina.com
  url: 'https://lfbear.com'
author_login: fbbear
author_email: fbbear@sina.com
author_url: 'https://lfbear.com'
wordpress_id: 447
wordpress_url: 'https://lfbear.com/?p=447'
date: '2013-07-27 22:35:26 +0800'
date_gmt: '2013-07-27 14:35:26 +0800'
categories:
  - 工作心语
tags:
  - angularjs
  - framework
comments: []
abbrlink: 63456
---
<p>最近在使用angularjs，感受一下用它来制作后台的便捷，的确值得一试。这里分享一个angularjs最常用的指令ng-repeat（类似与php中的foreach，js中的for）使用细节上的小问题。</p>
<p>ng-repeat可以用于js的数组和对象，可以对其中的元素进行遍历，当我首次使用ng-repeat的时候，只想对一个简单数组进行遍历（数据结构决定了我会使用很多js简单对象来存储数据），但是刚刚开始就发现了问题。<a href="http://plnkr.co/edit/dSJTc1yIjXrwIXKU2o0G?p=preview" target="_blank">猛戳这里在线demo</a>&nbsp;，代码如下：<br />
js部分</p>
<!-- more -->
<pre class="brush:javascript">$scope.list = [&#39;item1&#39;,&#39;item2&#39;,&#39;item3&#39;];</pre>
<p>&nbsp;</p>
<p>html部分</p>
<pre class="brush:php"><ul> 
  <li ng-repeat="item in list">
    <input type="text" value="{{item}}" ng-model="list[$index]" />
  </li>
</ul></pre>
<p>&nbsp;</p>
<p>在demo中，可以发现，input的显示是没有问题，但是编辑里面内容的时候，会发现任意修改之后，马上input就失去了焦点，无法正常编辑（后来研究了一下，貌似是因为angularjs底层的watch做的怪）。然后翻遍了angularjs的document和stackoverflow，竟然没有解决办法，stackoverflow唯一靠谱的替代方案把简单数组转成如下结构，该问题得到解决。</p>
<pre class="brush:javascript">$scope.list = [
    { val: &#39;item1&#39;},
    { val: &#39;item2&#39;},
    { val: &#39;item3&#39;}
]</pre>
<p>&nbsp;</p>
<p>但是这样改变了数据结构，很不爽。所以去angularjs的github里面提了suggest，得到一个汗颜的答案，angularjs的代码维护人员让我去使用angularjs的最新版本（官网的document竟然不是最新版的，被坑了）在最新版本中，angularjs发现了ng-repeat的这个遗漏，因此新加了一个track by的语法。<a href="http://plnkr.co/edit/AKsvCrs5fxD1nnBlT6Hc?p=preview" target="_blank">猛戳这里查看修正后的demo</a></p>
<p>这里，除了想告诉大家ng-repeat的使用细节以外，也要告诉大家，由于angularjs目前仍处在旺盛的青春期（当然，如果你想使用一款成熟的framework请绕路），请一定要使用http://code.angularjs.org/ 中的最新版本文档，当前最新在这里 http://code.angularjs.org/1.1.5/docs/。还有，google的产品似乎很喜欢使用googlegroups的maillist做问题交流，也请同学留意习惯。</p>
<p>可能有些人会觉得我这篇文章比较无聊，一个这么小的问题，至于花费时间去研究么，找个替代方案多好啊。但是我觉得使用framework就是这样，因为他不同于toolkit，当你准备好接受人家给你提供的便捷时，也一定要接受随之而来的束缚，接受framework的思想模式。任何不尊重framework的行为（包含语言攻击或者不按照规范使用）都是应该受到鄙视的。因为每个人的思维模式都不同，所以framework中呈现出来的思维也是不同的，有本事自己写个framework不要用人家的，或者干脆去用toolkit。每种思维模式都应该得到尊重，因为他是在特定环境和个人成长中产生的，也正因为此，世界才如此缤纷多彩。</p>
