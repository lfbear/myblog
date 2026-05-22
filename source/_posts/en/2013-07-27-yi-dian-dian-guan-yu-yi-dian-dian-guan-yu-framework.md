---
layout: post
status: publish
published: true
title: "A Little Bit About AngularJS, a Little Bit About Frameworks"
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
lang: en
---
Lately I've been using AngularJS to build a back-end dashboard, and experiencing the sheer convenience it offers. It's definitely worth giving a shot. Today, I want to share a subtle issue I encountered when using `ng-repeat`—one of Angular's most common directives (similar to `foreach` in PHP or a `for` loop in JS).

`ng-repeat` can be used on both JS arrays and objects to traverse their elements. When I first used it, I simply wanted to loop through a basic array (my data structure dictated that I'd use many simple JS objects/arrays to store data). However, I ran into a snag right off the bat. 

[Check out the live demo on Plnkr](http://plnkr.co/edit/dSJTc1yIjXrwIXKU2o0G?p=preview). The code is as follows:

**JS Part:**

<!-- more -->

```javascript
$scope.list = ['item1', 'item2', 'item3'];
```

**HTML Part:**

```html
<ul> 
  <li ng-repeat="item in list">
    <input type="text" value="{{item}}" ng-model="list[$index]" />
  </li>
</ul>
```

In the demo, you'll see that while the input displays perfectly initially, the moment you edit any character inside the input, the input immediately loses focus, making regular typing impossible. (After digging deeper, it turns out Angular's underlying `$watch` mechanism is behind this behavior). 

I searched through the AngularJS documentation and StackOverflow, but could barely find any standard solution. The only somewhat reasonable workaround on StackOverflow was to transform the primitive array into an array of objects like this:

```javascript
$scope.list = [
    { val: 'item1' },
    { val: 'item2' },
    { val: 'item3' }
]
```

But doing this requires changing my data structure, which felt incredibly dirty and unsatisfying. So, I went to the AngularJS GitHub repository to submit a suggestion, only to receive an answer that left me facepalming: the maintainer told me to use the latest version of AngularJS. (Turns out the official homepage documentation wasn't pointing to the latest version, quite a trap!). 

In the newer versions, the AngularJS team recognized this gap in `ng-repeat` and introduced the `track by` syntax. [Check out the corrected live demo here](http://plnkr.co/edit/AKsvCrs5fxD1nnBlT6Hc?p=preview).

Beyond sharing this technical quirk of `ng-repeat`, I also want to remind everyone that since AngularJS is still in its energetic "adolescent" phase (if you are looking for a completely mature, rock-solid framework, you might want to look elsewhere), you should always refer to the latest docs hosted at [http://code.angularjs.org/](http://code.angularjs.org/). At the time of writing, the latest is at [http://code.angularjs.org/1.1.5/docs/](http://code.angularjs.org/1.1.5/docs/). Additionally, Google products heavily rely on Google Groups mailing lists for community Q&A, which is another useful channel to keep in mind.

Some might think this post is incredibly trivial—why waste so much time digging into such a tiny issue when a quick workaround exists?

But I believe this is exactly what using a *framework* is all about. Unlike a *toolkit*, when you choose to embrace the conveniences a framework provides, you must also accept the constraints that come with it, and align yourself with the framework's design philosophy. Any behavior that disrespects a framework (including throwing tantrums or refusing to follow conventions) is missing the point. Every creator has a different mental model, and that model is reflected in the framework they design. If you don't like it, you are welcome to build your own framework from scratch, or just stick to toolkits. Every mental model deserves respect, as it is born out of a specific environment and personal growth. And that is exactly what makes the programming world so beautifully diverse.
