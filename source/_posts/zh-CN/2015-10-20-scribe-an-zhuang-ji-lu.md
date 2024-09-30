---
layout: post
status: publish
published: true
title: scribe 安装记录
author:
  display_name: 小飞熊
  login: fbbear
  email: fbbear@sina.com
  url: 'https://lfbear.com'
author_login: fbbear
author_email: fbbear@sina.com
author_url: 'https://lfbear.com'
wordpress_id: 489
wordpress_url: 'https://lfbear.com/?p=489'
date: '2015-10-20 16:31:00 +0800'
date_gmt: '2015-10-20 08:31:00 +0800'
categories:
  - 自言自语
tags: []
comments: []
abbrlink: 47685
---
<p>scribe是facebook的一款日志收集系统，看到fb瞬间觉得高大上的产品，但是整个安装历程很是坎坷啊，所以才把他记录下来，省得以后再次踩坑。</p>
<!-- more -->
<h3>1.&nbsp;系统依赖</h3>
<p>a、gcc和gcc-c++ (vision 4.1.2 pass)</p>
<p>b、ruby (vision 1.8.5 pass)</p>
<p>c、python (vision 2.4.3 pass) 含 python 和 python-devel</p>
<p>d、libevent (vision 1.4 pass) 含 libevent 和 libevent-devel</p>
<p>e、其他: openssl-devel, bison, autoconf(vision > 2.65), bzip2-devel, automake</p>
<p>可以使用这个来解决依赖</p>
<p>sudo yum install automake libtool flex bison pkgconfig gcc-c++ boost-devel libevent-devel zlib-devel python-devel ruby-devel openssl-devel</p>
<p><span style="text-decoration: underline;">一定不要着急装后面的组件 先把这些确认好 否则可能会重新安装 折腾起来更麻烦</span></p>
<h3>2. 安装前置组件</h3>
<div>boost &nbsp; 1.5.4</div>
<div>thrift &nbsp; &nbsp;0.9.0</div>
<div>fb303 &nbsp; &nbsp;thrift包中已包含</div>
<h4>2.1 安装 boost</h4>
<p>这是一个C++的标准库，用来后续编译c++代码使用</p>
<p>wget http://nchc.dl.sourceforge.net/project/boost/boost/1.45.0/boost_1_45_0.tar.bz2</p>
<p>tar jxvf boost_1_45_0.tar.bz2</p>
<p>cd boost_1_45_0</p>
<p>./bootstrap.sh</p>
<p class="p1"><span class="s1">./b2 install</span></p>
<p class="p1">。。。此过程巨慢 需要等待</p>
<p class="p1">默认安装到了/usr/local/include/boost/下</p>
<p>2.2 安装 thrift &amp; fb303</p>
<p>thrift同样是fb退出的一款框架，旨在打通多种语言程序之间的开发。</p>
<p>看到这里就知道了，其实fb的蓝图很大，为什么scribe不是一个单独的软件包了。安装了这些框架和编译库，你就有了fb的基础开发环境，当然fb之后的新东西也就0基础安装了。并且这也会传染其他开发者一起使用这套开发框架&hellip; 榜样作用嘛</p>
<p>A、trift安装</p>
<p>wget http://mirror.bjtu.edu.cn/apache/thrift/0.7.0/thrift-0.7.0.tar.gz</p>
<p>tar zxvf thrift-0.7.0.tar.gz</p>
<p>cd thrift-0.7.0.tar.gz</p>
<p>./configure CPPFLAGS="-DHAVE_INTTYPES_H -DHAVE_NETINET_IN_H"</p>
<p>make</p>
<p>make install</p>
<p>*configure时CPPFLAGS参数不可少，否则make时会产生诸如&ldquo;uint_32未定义&rdquo;之类错误。另外，configure时如找不到boost库，则需使用--with-boost参数指定boost库位置。thrift安装后可以进行简单的测试以确认是否安装成功。</p>
<p>B、fb303安装</p>
<p>cd contrib/fb303/</p>
<p>./bootstrap.sh</p>
<p>./configure</p>
<p>make</p>
<p>make install</p>
<p>C、运行一下thrift的例子（可选 这个步骤可以验证之前的组件是否都工作正常）</p>
<p>cd tutorial</p>
<p>thrift -r --gen cpp tutorial.thrift</p>
<p>cd cpp</p>
<p>make</p>
<p>./CppServer 可以启动Server</p>
<p>./CppClient 可以启动Client</p>
<h3>3. 安装scribe</h3>
<p>下载安装包 https://github.com/facebookarchive/scribe 并且解压进入目录</p>
<p>./bootstrap.sh</p>
<p>./configure (如上一条命令出现报错 请参见下面的特殊参数)</p>
<p>make</p>
<p>make install</p>
<p>报错看这里 基本上这里不保存的可能性不大</p>
<ul>
<li>典型错误 1</li>
</ul>
<div>configure时遇到</div>
<div></div>
<div>checking whether the Boost::System library is available&hellip; yes</div>
<div>checking whether the Boost::Filesystem library is available&hellip; yes</div>
<div>configure: error: Could not link against &nbsp;!</div>
<div></div>
<div><em>则需在configure时加上参数</em></div>
<div></div>
<div>--with-boost-system=lboost_system</div>
<div>--with-boost-filesystem=lboost_filesystem</div>
<ul>
<li>典型错误2</li>
</ul>
<div>
<div>make时遇到</div>
<div></div>
<div>undefined reference to 'boost::system::generic_category()'</div>
<div>undefined reference to 'boost::system::system_category()'</div>
<div></div>
<div><em>在确认boost::system库存在且路径正确后，检查GCC链接代码（根据make输出）</em></div>
<div>g++ &nbsp;-Wall -O3 -L/usr/local/lib/ -lboost_system -lboost_filesystem &nbsp;-o scribed store.o store_queue.o conf.o file.o conn_pool.o scribe_server.o network_dynamic_config.o dynamic_bucket_updater.o &nbsp;env_default.o &nbsp;-L/usr/local/lib -L/usr/local/lib -L/usr/local/lib -lfb303 -lthrift -lthriftnb -levent -lpthread &nbsp;libscribe.a libdynamicbucketupdater.a</div>
<div>此时需将-lboost_system -lboost_filesystem两个选项放在最后，并在src目录下手动执行链接即可完成编译。</div>
</div>
<p>我当时遇了上面的错误1，试验了好多种方法，终于得到了解决，最终我的configure参数是这样的</p>
<p>./configure --config-cache --prefix=/usr/local --with-boost=/usr/local/lib --with-boost-system=boost_system --with-boost-filesystem=boost_filesystem CPPFLAGS="-DHAVE_INTTYPES_H -DHAVE_NETINET_IN_H -DBOOST_FILESYSTEM_VERSION=3"</p>
<h3>4 参考资料</h3>
<ol>
<li>http://www.2cto.com/os/201307/224832.html</li>
<li>http://abentotoro.blog.sohu.com/190515962.html</li>
<li>http://www.linuxidc.com/Linux/2012-12/76340.htm</li>
<li>http://shiyanjun.cn/archives/107.html</li>
</ol>
