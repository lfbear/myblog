---
layout: post
status: publish
published: true
title: Docker Practices --- image & container
author:
  display_name: 小飞熊
  login: fbbear
  email: fbbear@sina.com
  url: 'https://lfbear.com'
author_login: fbbear
author_email: fbbear@sina.com
author_url: 'https://lfbear.com'
wordpress_id: 495
wordpress_url: 'https://lfbear.com/?p=495'
date: '2015-10-28 19:09:31 +0800'
date_gmt: '2015-10-28 11:09:31 +0800'
categories:
  - 工作心语
tags:
  - docker
  - image
  - container
comments: []
abbrlink: 22581
---
<p>关于docker的image和container，是docker初学者第一个比较困惑的概念。这里把关于image和container的一些使用心得分享出来，以便初学者能够快速了解。</p>
<p>本文旨在辅助初学者对docker的image和container做快速了解，并未对细节以及远离进行深入阐述，并由可能对真正的细节做了一些掩盖和曲解。了解更多，推荐阅读由Daniel Eklund的图解教程&nbsp;http://merrigrove.blogspot.hk/2015/10/visualizing-docker-containers-and-images.html，也是本文的参考文献之一（可能需要搭梯阅读）</p>
<!-- more -->
<h3>1.image （这里译为镜像）</h3>
<p>官方是这么解释image的：是container（译为容器）的基础，裸系统之上的<strong>每层文件系统变更</strong>的<strong>存档</strong>，镜像没有状态，也不会自己改变。</p>
<p><span style="color: #999999;"><em>原文：Docker images are the basis of containers. An Image is an ordered collection of root filesystem changes and the corresponding execution parameters for use within a container runtime. An image typically contains a union of layered filesystems stacked on top of each other. An image does not have state and it never changes.</em></span></p>
<p>在我看来，可以用虚拟机镜像来理解这个，我们平时使用虚拟机（无论是virtualbox还是VMware），都可以将之上装好的系统以文件的形式分享给别人。可以理解这个文件的形式就是镜像。当然docker的镜像细节上于它们还是有区别的，docker的镜像天然有版本信息在里面，每次容器的commit和save都会记录进去。</p>
<p>像&ldquo;洋葱皮&rdquo;一样，每save一次，外层就多了一层皮。很多docker初学者常常会迷惑一个问题，为什么image的尺寸（size）越来越大呢，做一些清理操作对尺寸也没什么影响。原因就是，新的洋葱皮只能在外面包（这里只是用洋葱这种植物举例，并非和洋葱的生长特性相同），每次都是增量保存文件系统的变更，而不是最终的状态。这样做的好处就是，方便你回退。</p>
<h3></h3>
<h3>2.container （这里译为容器）</h3>
<p>还是先来官方解释：是image（镜像）的运行实例，由镜像、运行环境和标准指令构成。概念借鉴于集装箱，集装箱是将全球船运标准化，docker的容器是定义<strong>一个软件承载方式的标准化</strong>。</p>
<p><span style="color: #999999;"><em>原文：A container is a runtime instance of a docker image.</em></span></p>
<p><span style="color: #999999;"><em>A Docker container consists of a Docker image, execution environment and standard set of instructions</em></span><br />
<span style="color: #999999;"><em>The concept is borrowed from Shipping Containers, which define a standard to ship goods globally. Docker defines a standard to ship software.</em></span></p>
<p>IMO，容器就是镜像的实例，一个动态的，运行时的东西，类似与高级语言中 new class。</p>
<p>但一定要记得，容器的特性决定了容器是一个随时可被销毁/替换的东西，一定不要指望把稳定的服务搭建在一个容器里（他们应该已经静态化到了镜像中，容器启动就可以启动服务）</p>
<p>另外：业务数据<strong>一定不要</strong>放到容器里，用docker的数据卷，这样在容器销毁的时候，数据还能保存下来，并且被另外一个替换容器继续使用。</p>
<h3>3.如何对待镜像和容器</h3>
<p>试想，如何你在电脑上写一本小说，当你觉得某一张终于写完了，为了对得起脑力的释放和体力的劳累，这时候必须要把这个文件保存起来。这个时候，你就应该考虑是不是要把容器保存成镜像了。docker&nbsp;commit 你的容器，并且save成镜像。</p>
<p>第二天，你又有了新的灵感，想要继续写作了。就在此时：</p>
<p>a.电脑没关，昨天那小说还在编辑状态：继续进入那个容器（start启动 或者 直接是exec执行命令）</p>
<p>b.电脑关掉了，开机并且找到那个小说的文件，打开继续写：容器被删除了，只能由 docker run命令再次生成一个。</p>
<p>上面的例子应该会对你有些启发吧，其实就是运行时和静态化的关系，如果想要运行，那就使用容器，想要做静态化保存为镜像。</p>
<h3></h3>
<h3>4、容器，镜像和静态文件的相互转换</h3>
<p><strong>a. 容器 - 镜像 - 文件</strong></p>
<p>导出：容器 <span style="color: #800080;">--[commit]--></span> 镜像 <span style="color: #800080;">--[save]--></span> .tar文件</p>
<p><em>commit 用法：sudo docker commit [容器名] [镜像名称]&nbsp;</em></p>
<p><em>save 用法：docker save -o&nbsp;[文件名].tar&nbsp;[镜像名称]</em></p>
<p>导入：容器 <span style="color: #3366ff;"><--[run]--</span> 镜像 <span style="color: #3366ff;"><--[load]--</span> .tar文件</p>
<p><em>run 用法：sudo docker run -t -i &nbsp;[镜像名称] /bin/bash</em></p>
<p><em>load 用法：sudo docker load <&nbsp;[文件名].tar</em></p>
<p><strong>b.容器 - 文件 - 镜像</strong></p>
<p>容器 &nbsp;<span style="color: #808000;">--[export]--></span> 文件 <span style="color: #808000;">--[import]--></span> 镜像</p>
<p><em>export 用法：sudo&nbsp;docker export [容器ID或名称]&nbsp;> [文件名].tar</em></p>
<p><em>import 用法：cat [文件名].tar | sudo&nbsp;docker import -&nbsp;[镜像名称]</em></p>
<p>&nbsp;</p>
<h3>#文献参考</h3>
<p>a.Visualizing Docker Containers and Images &nbsp;http://merrigrove.blogspot.hk/2015/10/visualizing-docker-containers-and-images.html</p>
<p>b.官方文档&nbsp;https://docs.docker.com/</p>
<p>c.《Docker 从入门到实践》线上版本 &nbsp;http://dockerpool.com/static/books/docker_practice/index.html</p>
