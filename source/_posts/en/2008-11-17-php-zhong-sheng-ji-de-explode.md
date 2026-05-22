---
layout: post
lang: en
status: publish
published: true
title: An Upgraded explode() Function in PHP
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
In PHP, the `explode()` function splits a string into an array by a specified delimiter. Those who use this function regularly might have run into situations where the string contains the delimiter in parts you *don't* actually want to split. For instance, splitting `name|pass` by `|` is completely fine, but if you have a string like `myuser|pass|123`, then `pass` and `123` will also be split apart. I encountered exactly this issue at work today, so I wrote a little helper function to handle it. <!--more-->

Let's look at an example. Say we have a string:

`$s = 'myinfo|myname|mypass|12|3|456|789';`

Suppose `12|3` is the section we want to keep intact as a single block. We can solve this with our helper like this:

`$rs = adv_explode($s, '|', 3, 2);` 

This means: split `$s` using `|` as the delimiter, keeping the first 3 segments and the last 2 segments as normal splits, and merging whatever is left in the middle. Haha, I didn't include any strict parameter validation, so feel free to add that yourself if you need it. The code is actually very simple, written just to make life a bit easier for everyone!

```php
/**
 * adv_explode Splits a string based on specific index boundaries
 *
 * Detailed Description
 * @param string $str The string to split
 * @param string $split The delimiter
 * @param int $a Number of normal split elements to keep from the front
 * @param int $b Number of normal split elements to keep from the back
 * @return array
 */
function adv_explode($arr, $split, $a, $b)
{
    $arr = explode($split, $arr);
    $k = 0;
    for ($i = 0; $i < count($arr); $i++) {
        if ($i <= $a - 1) {
            $re[$i] = $arr[$i];
        } else if ($i >= count($arr) - $b) {
            $j = $i - (count($arr) - $a - $b - 1);
            $re[$j] = $arr[$i];
            unset($j);
        } else {
            $tmp[$k] = $arr[$i];
            $k++;
        }
    }
    if ($k > 1) {
        $re[$a] = implode($split, $tmp);
    } else {
        $re[$a] = $tmp[0];
    }
    return $re;
}
```
