---
layout: post
status: publish
published: true
title: "Key Takeaways: Building High-Performance Web Pages & Understanding Analytics"
author:
  display_name: 小飞熊
  login: fbbear
  email: fbbear@sina.com
  url: 'https://lfbear.com'
author_login: fbbear
author_email: fbbear@sina.com
author_url: 'https://lfbear.com'
excerpt: 收获
wordpress_id: 57
date: '2008-12-17 15:55:06 +0800'
date_gmt: '2008-12-17 07:55:06 +0800'
categories:
  - 工作心语
tags:
  - 收获
  - 优化
  - web
comments: []
abbrlink: 31439
lang: en
---
Recently, our company organized two training sessions. I'm writing down some of my key takeaways here (not the direct training slides, but my own summaries and thoughts), so I don't end up forgetting them over time~ Feel free to share your thoughts—knowledge only grows when we exchange it!

<!--more-->

### Mission 1: High-Performance Web Pages

I'm sure everyone has been there: opening a webpage, waiting forever, only to end up with "This page cannot be displayed" or seeing only a broken, partially loaded page. This kind of experience is incredibly frustrating for users. While there can be many culprits—sometimes client-side issues—the majority of the time, the bottleneck lies on the server side. 

So, here are a few tips on server-side optimization, primarily geared toward front-end developers (including RIA developers and page builders).

#### 1. Minimize HTTP Requests as Much as Possible
Anyone who has studied networking knows that HTTP is an application layer protocol. Too many HTTP requests inevitably lead to an excessive number of TCP/IP connections. And as we all know, establishing a TCP/IP connection requires a three-way handshake! Therefore, reducing HTTP requests directly cuts down network communication overhead, thereby speeding up page load times.

A single HTML/HTM page counts as one HTTP request, and every image, Flash, or external asset embedded in that page counts as an additional request. While reducing unnecessary elements is ideal, sometimes you might say: "But all of these are important, we can't just toss them out!" Okay, if we can't throw them out, we don't have to. Let's find another way.

A classic industry solution for optimizing images is using **CSS Sprites**: combining all small images into a single larger image file, and then using CSS positioning (`background-position`) to display the specific image needed. This is a tried-and-true method used by countless websites. One single HTTP request to handle all small images!

#### 2. Reducing TCP/IP Connections Directly
*   **a. Enable Keep-Alive**: Ensure `Keep-Alive` is enabled in your HTTP headers (if supported by your server).
*   **b. Implement Smart Caching**: For static resources, you can set the cache expiration date to never expire. For dynamic resources, set appropriate expiration times based on requirements. *(Here's a little secret commonly used by industry pros: set static resources to never expire, but append a version number to the filename—for example, naming `my.js` as `my_0.1.0.js`. This way, whenever you update static resources, users get the latest version immediately without any cache-busting pain).*
*   **c. Socket Reuse**: This depends highly on your server environment. Interested folks can Google this (full disclosure: I'm not an expert on this one either, haha).
*   **d. Limit Subdomain Variety**: It's generally best to keep the number of subdomains between 4 to 8, depending on traffic volume and load balancing configurations.

#### 3. Use Gzip Compression
Enable Gzip compression on the server to compress data sent over the network, saving precious bandwidth. Most modern servers support Gzip right out of the box. However, that doesn't mean you should compress absolutely everything. 

*Recommended strategy*: Use it for text-based files that are at least a few kilobytes in size (e.g., JS, HTML, XML). Compressing JPEG images with Gzip makes zero sense.

#### 4. CSS at the Top, JS at the Bottom (See resources at the end for details)

#### 5. Disable ETags Under Load Balancing (See resources at the end for details)

---

### Mission 2: What Does Your Site Actually Need?

This section is all about data analysis and analytics. Specifically, putting tracking codes on live products to monitor traffic and taking action when anomalies occur. This is a fantastic habit. While large-scale websites can build their own custom internal monitoring systems, for small-to-medium sites or personal blogs, I highly recommend using Google Analytics ([http://www.google.com/analytics/](http://www.google.com/analytics/)). It's an outstanding system that is definitely worth trying.

**The Goal**: The goal of data analysis is simple—identify your enemies (those maliciously scraping/draining your resources) and your friends (legitimate users). 
*   What do you do if you get too many enemies? You tighten up your security mechanisms and implement rate limiting.
*   What do you do when you get more friends? You scale up your servers, deploy CDNs, and optimize performance to keep their experience smooth.
*   Additionally, looking at historical data allows you to make predictions, such as anticipating traffic spikes during breaking news or identifying traffic trends during specific times of the day.

**In a Nutshell**: You need to know not only *what* you are building, but also *how* well it is performing. Use periodic statistical results and predictions to drive and optimize your strategy for the next phase!

---

**Resource Download**: [High-Performance Web Pages Tutorial](/assets/images/20081226_117427.rar)
