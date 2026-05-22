---
layout: post
status: publish
published: true
title: I Wrote a Very Wicked Piece of Code
lang: en
author:
  display_name: 小飞熊
  login: fbbear
  email: fbbear@sina.com
  url: 'https://lfbear.com'
author_login: fbbear
author_email: fbbear@sina.com
author_url: 'https://lfbear.com'
wordpress_id: 62
wordpress_url: 'https://lfbear.com/?p=62'
date: '2008-11-14 10:47:29 +0800'
date_gmt: '2008-11-14 02:47:29 +0800'
categories:
  - 程序人生
tags:
  - php
  - 外挂
comments:
  - id: 242
    author: countmeon
    author_email: countmeon@gmail.com
    author_url: 'http://pzg.me/'
    date: '2009-10-30 14:57:49 +0800'
    date_gmt: '2009-10-30 06:57:49 +0800'
    content: 呵呵  过于专业了
abbrlink: 5337
---
To be honest, as a game developer, I absolutely despise game exploits and bots (外挂) because they ruin all the fun and cause games to die out prematurely. I really didn't want to go down this road, but my slot machine account was completely broke, so I was forced to write a bot for it. Since yours truly (熊熊 - Beary) is the author of this slot machine app, I won't be posting the complete code here (P.S. If everyone starts exploiting my slot machine, I'll probably get assigned the task of adding anti-cheat mechanisms. Gotta save myself some extra work, hehe!). However, I *will* teach you guys how to write a bot for web games using PHP.

<!--more-->

Conceptually, game bots are actually very simple: you're just writing code to let a machine replace a human to perform repetitive, predictable actions. So while a bot is a godsend for gamers, for programmers it's just a little helper to give ourselves a break, haha~ (Below is the core logic of my bot program):

```php
$ch = curl_init();      
curl_setopt($ch, CURLOPT_REFERER, 'http://xxx');  
curl_setopt($ch, CURLOPT_URL, 'http://yyy');   
curl_setopt($ch, CURLOPT_POST, 1);  
curl_setopt($ch, CURLOPT_POSTFIELDS, $postdata);      
curl_setopt($ch, CURLOPT_COOKIEFILE, $cookiefile);      
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);      
curl_setopt($ch, CURLOPT_HEADER, false);      
curl_setopt($ch, CURLOPT_NOBODY, false);      
$re = curl_exec($ch);      
curl_close($ch);    
```

Getting back to business—in PHP, we primarily use the cURL library to spoof a browser, making frequent, patterned requests to specific scripts. The cURL workflow starts with `curl_init()`, configures spoofing parameters using `curl_setopt()`, executes the request via `curl_exec()`, and finally wraps up with `curl_close()`. Isn't the workflow simple? I'll append a list of common `curl_setopt` options along with their explanations at the end of this post (since `setopt` does most of the heavy lifting for spoofing). It can spoof logins and mimic almost any human action. It's incredibly powerful!~

Web-based social games are usually built around you and your friends, so step one is fetching your friend list. This is typically done by sniffing the network traffic using Firefox paired with Firebug. Once you grab the data, clean it up and format it with a specific delimiter. OK, now that the program knows who you're playing with, the next step is using Firefox + Firebug again to capture the actual endpoint URL—specifically, the script where game actions are submitted (which I'll refer to as the "main game script"). 

You'll target that URL using line 3 in the snippet above, and use lines 4 and 5 to send your POST data (e.g., `$postdata = 'act=play&money=123&...'` where multiple parameters are joined by ampersands). If it's a GET request, it's even simpler—just append the query parameters directly to the URL. 

Line 7 (`CURLOPT_RETURNTRANSFER`) is responsible for returning the server's response into `$re`, allowing us to parse the response and decide what to do next. *Note: Server responses are usually encoded. Common formats include JSON, XML, or serialized PHP arrays, so remember to decode them before parsing!*

You might be wondering about the purpose of lines 2 and 6. These are the core spoofing layers. Line 2 (`CURLOPT_REFERER`) mocks the referrer header; main game scripts often check this to ensure the request originated from an authorized game page. Line 6 (`CURLOPT_COOKIEFILE`) loads the cookies of an authenticated session (likewise, you can capture cookies in a script by adding `curl_setopt($ch, CURLOPT_COOKIEJAR, $cookiefile);`). This tells the main game script that you are indeed a logged-in user.

That's the general process! The rest is just wrapping this snippet in a loop (to iterate over all your friends), handling response assertions, adjusting parameters, or redirecting as needed. Different web games might employ different filters or validation checks, so I highly recommend playing through the game once while logging the entire flow in Firebug before writing any bot code. Otherwise, it's very easy to run into roadblocks!~

If there's anything I didn't explain clearly, feel free to drop a comment and chat tech with yours truly! Below is a list of commonly used `curl_setopt` parameters (sourced from the web, shoutout to the original translator):

### curl_setopt Option Reference

`bool curl_setopt (int ch, string option, mixed value)`

The `curl_setopt()` function sets an option for a cURL session. The `option` parameter is the setting you want, and `value` is the value given to this option.

**The following options expect integer/boolean values:**

*   **CURLOPT_INFILESIZE**: When uploading a file to a remote site, this option tells PHP the size of the uploaded file.
*   **CURLOPT_VERBOSE**: Set this to a non-zero value if you want cURL to report every event/detail.
*   **CURLOPT_HEADER**: Set this to a non-zero value if you want to include headers in the output.
*   **CURLOPT_NOPROGRESS**: Set this to a non-zero value if you don't want PHP to display a progress bar for cURL transfers. Note: PHP sets this to non-zero by default; you should only change it for debugging purposes.
*   **CURLOPT_NOBODY**: Set this to a non-zero value if you don't want to include the body in the output.
*   **CURLOPT_FAILONERROR**: Set this to a non-zero value if you want PHP to fail silently on errors (HTTP status code >= 300). The default behavior returns the normal page, ignoring the error code.
*   **CURLOPT_UPLOAD**: Set this to a non-zero value if you want PHP to prepare for an upload.
*   **CURLOPT_POST**: Set this to a non-zero value if you want PHP to perform a regular HTTP POST. This POST uses the standard `application/x-www-form-urlencoded` format, typically used by HTML forms.
*   **CURLOPT_FTPLISTONLY**: Set this to a non-zero value to list only directory names for FTP.
*   **CURLOPT_FTPAPPEND**: Set this to a non-zero value to append to the remote file instead of overwriting it.
*   **CURLOPT_NETRC**: Set this to a non-zero value to make PHP look up credentials in your `~/.netrc` file for the remote connection.
*   **CURLOPT_FOLLOWLOCATION**: Set this to a non-zero value to follow "Location:" headers sent by the server (note that this is recursive; PHP will follow redirects).
*   **CURLOPT_PUT**: Set this to a non-zero value to upload a file via HTTP. To upload the file, the `CURLOPT_INFILE` and `CURLOPT_INFILESIZE` options must also be set.
*   **CURLOPT_MUTE**: Set this to a non-zero value to suppress all cURL outputs in PHP.
*   **CURLOPT_TIMEOUT**: Set a long integer value specifying the maximum number of seconds to allow cURL functions to execute.
*   **CURLOPT_LOW_SPEED_LIMIT**: Set a long integer controlling the minimum transfer speed in bytes per second.
*   **CURLOPT_LOW_SPEED_TIME**: Set a long integer specifying the number of seconds the speed must be below `CURLOPT_LOW_SPEED_LIMIT` before aborting.
*   **CURLOPT_RESUME_FROM**: Pass a long integer specifying the byte offset to resume the transfer from.
*   **CURLOPT_SSLVERSION**: Pass a long integer containing the SSL version. By default, PHP will try to determine this automatically, but for tighter security, you can set it manually.
*   **CURLOPT_TIMECONDITION**: Pass a long integer specifying how to handle the `CURLOPT_TIMEVALUE` parameter. You can set this to `TIMECOND_IFMODSINCE` or `TIMECOND_ISUNMODSINCE`. (HTTP only).
*   **CURLOPT_TIMEVALUE**: Pass the number of seconds since January 1, 1970. This timestamp is used by `CURLOPT_TIMECONDITION`.

**The following options expect string values:**

*   **CURLOPT_URL**: The URL you want PHP to fetch. You can also set this when initializing with `curl_init()`.
*   **CURLOPT_USERPWD**: A string formatted as `[username]:[password]` for authentication.
*   **CURLOPT_PROXYUSERPWD**: A string formatted as `[username]:[password]` for HTTP proxy authentication.
*   **CURLOPT_RANGE**: A range of bytes to retrieve, formatted as `X-Y` (inclusive). cURL also supports multiple intervals separated by commas (e.g., `X-Y,N-M`).
*   **CURLOPT_POSTFIELDS**: A string containing the full data to be sent in an HTTP POST request.
*   **CURLOPT_REFERER**: A string to be sent in the "Referer" header of the HTTP request.
*   **CURLOPT_USERAGENT**: A string to be sent in the "User-Agent" header of the HTTP request.
*   **CURLOPT_FTPPORT**: A string containing the IP address to be used by the FTP "PORT" command. This tells the remote server to connect back to our specified IP. This can be an IP address, a hostname, a network interface name, or `-` to use the system default.
*   **CURLOPT_COOKIE**: A string containing the cookie header to send with the HTTP request.
*   **CURLOPT_SSLCERT**: A string containing the path to a PEM-formatted certificate.
*   **CURLOPT_SSLCERTPASSWD**: A string containing the passphrase required to use the certificate specified by `CURLOPT_SSLCERT`.
*   **CURLOPT_COOKIEFILE**: A string containing the path to a file containing cookie data. This file can be in Netscape format or standard HTTP header format.
*   **CURLOPT_CUSTOMREQUEST**: A custom request method to use instead of GET or HEAD. Make sure your server supports it before using it.

**The following options expect a file resource (returned by `fopen()`):**

*   **CURLOPT_FILE**: The file where the transfer output should be written. Defaults to STDOUT.
*   **CURLOPT_INFILE**: The input file for file uploads.
*   **CURLOPT_WRITEHEADER**: The file where the response header portion should be written.
*   **CURLOPT_STDERR**: The file to write error messages to instead of stderr.
