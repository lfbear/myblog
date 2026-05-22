---
title: Switching Over to Hexo
tags:
  - hexo
  - blog
categories:
  - 自言自语
abbrlink: 50111
date: 2020-03-15 21:41:52
lang: en
---
My blog hasn't been updated for over a year. Truth be told, I went through a lot in 2019 and had so many reflections. But every time I wanted to write, Jekyll's friction made it a hassle to use, so I kept putting it off.

Then, during the 2020 Spring Festival, I stumbled upon [Hexo](https://hexo.io/) and my eyes lit up. The ecosystem is so vibrant and thriving! I spent a bit of free time over the weekend writing a script to migrate all my past posts, and it worked like a charm.

Here are a few frequently used Hexo commands to save my future self from forgetting them the next time I write:

```shell
hexo new [layout] <title> # Create a new blog post
hexo clean                # Clean generated cache/static files
hexo g                    # Generate static files
hexo s                    # Start the local server
```

Let's test it out and see if it's as convenient as it looks. Also, a huge shout-out to Travis CI for providing their free CI/CD build services—with the size of my blog, it builds in under a minute.
