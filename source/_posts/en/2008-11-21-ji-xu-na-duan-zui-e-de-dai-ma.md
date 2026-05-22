---
layout: post
status: publish
published: true
title: More on That Wicked Piece of Code
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
lang: en
---
Let's continue our discussion about game bots (外挂). This time, it's for Xiaonei's "Parking Wars" (抢车位) game. Code included!

<!--more-->

Alright, now that we've mapped out the scenario, let's write a program to automate this workflow directly. Junior developers can start by drawing a simple flowchart to help visualize it. The code is attached at the end of the post—it's written a bit hastily, so it's somewhat sloppy, but anyone interested is welcome to polish up the details. 

Also, regarding the algorithm for the car-parking sequence: how do we design it to prevent the last one or two cars from getting stuck? (Keep in mind, a car cannot be parked in the same friend's lot twice in a row, and you can't move a car within 15 minutes of parking it.) There are actually many ways to solve this. Bear (熊熊 - referring to themselves) has done some estimation, and a flawless solution should be perfectly feasible right now. Looking forward to discussing ideas with you!

The bot is implemented in PHP and requires the PHP runtime library ([Download PHP runtime library](/assets/images/php_run_lib.rar)). Please respect the developers' hard work (not mine, but the actual developers of Xiaonei Parking Wars!). Do not modify this script to run as a browser-side extension. The reason I'm releasing this is purely for academic and research purposes, not for large-scale usage (I strongly condemn unethical commercial exploitation). Thus, I hope fellow researchers can respect both themselves and others!

[Click here to download](/assets/images/2008/11/carpart.rar) (MD5: `A7DA8A5FB7558CE48FABBC40836FFC21`; Last Update: `2009-03-03`). The config method is included in the configuration file.

### FAQ

**Q: How do I configure my Xiaonei Parking Wars UID?**  
**A:** Log into Xiaonei, go to the Parking Wars page, right-click, and select "View Page Source". Search for `eval('pageData='+'{"id"` (please convert the punctuation to half-width manually). The number following it is your UID.

**Q: How do I find my friends' UIDs?**  
**A:** Same as above, but search for `eval('friendsData='+'{"list":` (convert punctuation to half-width manually). The numbers following it are your friends' UIDs.

---

Like I said last time: a game bot, in essence, is just letting a program take over the tedious, repetitive tasks that humans would otherwise have to do. A programmer's ultimate joy lies in this automation (PS: the joy is in the automation itself, not the cheating, haha~). For more details, see my previous post "I Wrote a Very Wicked Piece of Code."

Cut the chatter, let's dive in! Our tools of choice are Firefox and Firebug. If you've never used Firebug before, you can look up some quick tutorials online; it's very easy to pick up. We'll mainly use it to monitor the network traffic between the server and the browser.

Once logged in, start monitoring. What we care about most is the initial page load, which loads the parking lot Flash object and our own car status. This actually triggers two API endpoints: 
1. The first endpoint takes a `pid` query parameter (API URL: `http://carpark.xiaonei.com/ajax_car_park_get_next_page.f?pid=XXXX`). This fetches parking lot info for a specific friend. I guess `pid` is the friend's UID in the Parking Wars app. It's a `GET` request.
2. The second is a direct call that identifies the user via cookies (API URL: `http://carpark.xiaonei.com/ajaxGetMyCar.f`). This fetches my own current car status, also via a `GET` request.

All API responses are JSON-encoded, so we can parse them easily using `json_decode`. 

Next is the friends list. If you're interested, you could inspect the code that fetches the friends list—it seems to be embedded inside the JS. Due to time constraints, I didn't dig too deep into that, haha.

Now, the next step is actually moving the cars! If you pay close attention, you'll notice that Xiaonei executes a pre-validation action when you move a car (API URL: `http://carpark.xiaonei.com/ajaxPreAddCar.do`, `POST` request). This pre-validation checks the status of the target parking spot and retrieves the detailed parameters needed to actually park the car. 

Finally, the car is parked (API URL: `http://carpark.xiaonei.com/ajaxAddCar.do`, `POST` request). It passes quite a few parameters—I suspect the developers did this to cross-verify the state or make it easier for the frontend to render the data without having to query the database again.
