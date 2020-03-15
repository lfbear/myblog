---
layout: post
status: publish
published: true
title: 继续那段罪恶的代码
author:
  display_name: 小飞熊
  login: fbbear
  email: fbbear@sina.com
  url: 'https://lfbear.com'
author_login: fbbear
author_email: fbbear@sina.com
author_url: 'https://lfbear.com'
excerpt: 外挂
wordpress_id: 52
date: '2008-11-21 16:50:04 +0800'
date_gmt: '2008-11-21 08:50:04 +0800'
categories:
  - 自言自语
tags:
  - php
  - 外挂
  - 游戏
comments: []
abbrlink: 36147
---
<p>继续来讲讲外挂，这次是校内的抢车位游戏，附代码。</p>
<p><!--more-->好了，情况都清楚了，直接写程序来走这个流程吧，初级程序写手可以先画一下简易的流程图来辅助，代码附在文后，因为时间仓促所以写得比较烂，有心人可以来把细节搞定一下，还有就是关于挪车序列的算法，怎么做这个算法才能避免最后一辆或者几辆车子没办法挪动的情况呢（同一辆车不允许连续停相同主人处，15分钟内不能挪车子）其实还有很多办法来解决这些问题，熊熊预估了一下，目前应该可以做到完美处理这个问题。欢迎交流哦~程序为php实现，需要使用运行库(<a title="php运行库" href="/assets/images/php_run_lib.rar" target="_blank">下载php运行库</a>)，请大家尊重开发者的辛勤劳动（不是偶，是校内抢车位的开发人员），不要将该程序改为浏览器端调用，之所以这样，其实完全是为了让这个程序用来研究，而不是大规模的使用（痛斥不道德的商业使用），因此，希望程序研究者能够尊重自己尊重他人！ <a href="/assets/images/2008/11/carpart.rar" target="_blank">点击下载</a> (md5:A7DA8A5FB7558CE48FABBC40836FFC21;last update:2009-03-03) 配置文件内含配置方法。</p>
<p>faq:</p>
<p>Q:如何配置校内抢车位uid？</p>
<p>A:登录校内，打开抢车位页，右键查看源文件，搜索 eval('pageData='+'{"id"&nbsp; (标点符号请手动转为半角)后面的数字便是你的uid。</p>
<p>Q:如何找到好友的uid？</p>
<p>A:同上，搜索 val('friendsData='+'{"list": 标点符号请手动转为半角)后面的数字便是好友的uid。</p>
<p>---------------------------------------------------------------------------------------<br />
还是上次那句话，所谓外挂，就是让程序代替人来完成累人的活儿，程序员最大的乐趣便在此（ps：乐趣不在外挂哦，哈哈~）。详见《写了一段很罪恶的代码》一文。<br />
废话少说，开始啦，工具是firefox+firebug 如果是第一次用可以参考下网上的教程，很容易上手的。主要用它来监视服务器与浏览器的交互过程。<br />
登录后，开始监视，比较关心的是页面载入的时候会加载车位的flash和自己的车子的情况 其实这是调用了两个接口，上面那个指定的uid参数（接口地址：<a href="http://carpark.xiaonei.com/ajax_car_park_get_next_page.f?pid=XXXX">http://carpark.xiaonei.com/ajax_car_park_get_next_page.f?pid=XXXX</a>获取某好友停车场信息，pid猜测可能为用户在停车位中的uid，get调用），看对方车位的状况，下面是直接调用，通过cookie作为识别（接口地址：<a href="http://carpark.xiaonei.com/ajaxGetMyCar.f">http://carpark.xiaonei.com/ajaxGetMyCar.f</a>获取目前我自己的车的信息，get调用）。所有返回均为json编码，做一下json_decode就可以了。然后是好友列表，有心人可以去抓一下好友列表的程序，貌似夹在了js里面，时间原因，我没去研究，呵呵。好了，下一步就是挪车子啦，细心的你也许会发现，校内挪车子的时候有一个预操作（接口地址：<a href="http://carpark.xiaonei.com/ajaxPreAddCar.do">http://carpark.xiaonei.com/ajaxPreAddCar.do</a> post调用），通过预操作来确认车位的状态和获取挪车子用的详细信息，然后就是挪车子了（接口地址：<a href="http://carpark.xiaonei.com/ajaxAddCar.do">http://carpark.xiaonei.com/ajaxAddCar.do</a>，post调用）指定的参数较多，估计是开发者为了校对信息或者方便界面获取数据（不再调用数据库）使用吧~</p>
