---
layout: post
status: publish
published: true
title: python学习笔记-1
author:
  display_name: 小飞熊
  login: fbbear
  email: fbbear@sina.com
  url: 'https://lfbear.com'
author_login: fbbear
author_email: fbbear@sina.com
author_url: 'https://lfbear.com'
wordpress_id: 291
wordpress_url: 'https://lfbear.com/?p=291'
date: '2009-03-04 17:14:44 +0800'
date_gmt: '2009-03-04 09:14:44 +0800'
categories:
  - 工作心语
tags:
  - python
  - 学习笔记
comments:
  - id: 76
    author: 刘炜
    author_email: xisuosunboy@126.com
    author_url: ''
    date: '2009-04-07 09:53:39 +0800'
    date_gmt: '2009-04-07 01:53:39 +0800'
    content: python 呵呵 2.5+ 哈
abbrlink: 35722
---
<p>入门课程 主要记录python的数据类型和基本函数</p>
<p><!--more--></p>
<p>1.数据类型</p>
<p>--------------------</p>
<p>a.字典 Dictionary</p>
<p>$定义</p>
<p>d = {key1:value1,key2:value2....} 定义时使用{} key与value之间用:分隔，每一个元素都是一个 key-value 对，多个元素用,分隔。</p>
<p>$约束</p>
<p>key是唯一的(大小写敏感)，为已有key复制将覆盖原值；<br />
字典中的元素是无序的；<br />
字典中元素的值可以是任意数据类型。</p>
<p>$操作</p>
<p>赋值</p>
<p>d['newkey'] = newvalue</p>
<p>删除单个元素</p>
<p>del d['newkey']</p>
<p>清空字典</p>
<p>d.clear()</p>
<p>-----</p>
<p>b.列表 List</p>
<p>$定义(可理解为数组)</p>
<p>l = [a,b,c....] 定义时使用[] 每个元素用,分隔。</p>
<p>$约束</p>
<p>元素是有序的<br />
非空List第一个元素为l[0] 一个含有n个元素的List 最后一个元素为l[n-1] 或 l[-1]；<br />
List允许索引为负值 负值是从尾部向前计数来取元素；<br />
List中元素的值可以是任意数据类型。</p>
<p>$分片</p>
<p>指定2个索引值来得到List的子集，l[0:3] 返回 list 的前 3 个元素 : 前后索引均可省略，分别默认为0 和 -1。</p>
<p>$操作</p>
<p>增加</p>
<p>l.append('new') 向list尾部增加一个元素。</p>
<p>l.insert(1,'new') 指定索引增加一个元素，该元素后面的元素索引会自动向后移动一个位置。</p>
<p>l.extend(["two", "elements"]) 连接2个List，注意extend的参数为list，新元素会在尾部。</p>
<p>搜索</p>
<p>l.index('a') 在 list 中查找一个值的首次出现并返回索引值，如果在 list 中没有找到值，Python 会引发一个异常。</p>
<p>'a' in l 要测试一个值是否在 list 内，使用 in。如果值存在，它返回 True，否则返为 False 。</p>
<p>删除</p>
<p>l.remove('a') 删除首次出现的值</p>
<p>l.pop() 删除最末尾的元素，并返回。</p>
<p>List 运算</p>
<p>+ 运算符连接起来相当于extend，但大型list使用extend会快一些<br />
* 运算符 相当于将原来的list重复作用于新的list</p>
<p>-----</p>
<p>c.元组 Tuple 即为不可更改的List</p>
<p>$定义</p>
<p>t = ('a','b','c') 定义时使用() 每个元素用,分隔。</p>
<p>$约束</p>
<p>Tuple 不能使用增、删、查操作</p>
<p>$好处</p>
<p>Tuple 使用比List 快，适合存放常量<br />
安全，可以转换为List，反之不可以<br />
可以作为字典的key，List则不可以，以为List可变<br />
Tuples 可以用在字符串格式化中</p>
<p>--------------------<br />
2.函数定义</p>
<p>def function(parameter1,parameter2,...):<br />
函数体需要缩进</p>
<p>$一些有用的函数</p>
<p>type 函数：返回任意对象的数据类型。<br />
str 函数：将数据强制转换为字符串。<br />
dir 函数：查看对象可进行的操作。<br />
callable 函数：对象是否可以调用。<br />
getattr 函数：获取对象引用，可用于分发，自省的核心。</p>
<p>$其他知识</p>
<p>python的内置函数在 __builtin__ 模块中</p>
<p>学习教程：dive into python 一本很好的书</p>
