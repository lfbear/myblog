---
layout: post
status: publish
published: true
title: "Facebook Scribe Installation Notes"
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
lang: en
---
Scribe is Facebook's log collection system. The moment you see "FB", you immediately think it's a high-end, top-tier product. However, the entire installation journey was incredibly bumpy! So, I'm writing down these setup notes to save my future self from falling into the same traps again.

<!-- more -->

### 1. System Dependencies

*   **a. GCC and GCC-C++** (version 4.1.2 tested and passed)
*   **b. Ruby** (version 1.8.5 tested and passed)
*   **c. Python** (version 2.4.3 tested and passed, including both `python` and `python-devel`)
*   **d. libevent** (version 1.4 tested and passed, including both `libevent` and `libevent-devel`)
*   **e. Others**: `openssl-devel`, `bison`, `autoconf` (version > 2.65), `bzip2-devel`, `automake`

You can resolve all of these dependencies using yum:
```bash
sudo yum install automake libtool flex bison pkgconfig gcc-c++ boost-devel libevent-devel zlib-devel python-devel ruby-devel openssl-devel
```

> [!IMPORTANT]
> **Please do not rush into installing the later components before verifying these!** Make sure these dependencies are properly confirmed first, otherwise you might end up having to reinstall, which makes things ten times more frustrating.

---

### 2. Pre-requisite Components

*   **Boost**: `1.5.4`
*   **Thrift**: `0.9.0`
*   **fb303**: Already included inside the Thrift package

#### 2.1 Installing Boost

This is a C++ standard library, required for compiling C++ code later on.
```bash
wget http://nchc.dl.sourceforge.net/project/boost/boost/1.45.0/boost_1_45_0.tar.bz2
tar jxvf boost_1_45_0.tar.bz2
cd boost_1_45_0
./bootstrap.sh
./b2 install
```
*Note: This compiling step is incredibly slow. Be prepared to wait.*

By default, it will be installed under `/usr/local/include/boost/`.

#### 2.2 Installing Thrift & fb303

Thrift is another framework released by Facebook, designed for seamless development and RPC between programs written in different languages.

Seeing this, it becomes clear that Facebook's blueprint is massive. This explains why Scribe isn't just a simple, standalone package. Once you've set up these frameworks and compiled libraries, you essentially have Facebook's foundational development environment ready. Any subsequent FB tool you install will be a breeze, starting from a warm baseline. Plus, it naturally encourages other developers to adopt the same framework... talk about leading by example!

**A. Thrift Installation**
```bash
wget http://mirror.bjtu.edu.cn/apache/thrift/0.7.0/thrift-0.7.0.tar.gz
tar zxvf thrift-0.7.0.tar.gz
cd thrift-0.7.0
./configure CPPFLAGS="-DHAVE_INTTYPES_H -DHAVE_NETINET_IN_H"
make
make install
```
*Note: The `CPPFLAGS` argument is mandatory when running `configure`. Otherwise, the compilation will fail during `make` with errors like 'uint_32 undefined'. Additionally, if the configuration step cannot find the Boost library, you must specify its location using the `--with-boost` parameter. After installing Thrift, it's a good idea to run a quick test to verify it works.*

**B. fb303 Installation**
```bash
cd contrib/fb303/
./bootstrap.sh
./configure
make
make install
```

**C. Run a Thrift Example (Optional—good for verifying components are working properly)**
```bash
cd tutorial
thrift -r --gen cpp tutorial.thrift
cd cpp
make
./CppServer  # Starts the server
./CppClient  # Starts the client
```

---

### 3. Installing Scribe

Download the package from [https://github.com/facebookarchive/scribe](https://github.com/facebookarchive/scribe), extract it, and navigate into the directory:
```bash
./bootstrap.sh
./configure   # If this errors, please check the special parameters below!
make
make install
```

#### Troubleshooting Common Compilation Errors (Chances are high you will run into these):

*   **Typical Error 1**:
    During `configure`, you encounter:
    ```text
    checking whether the Boost::System library is available… yes
    checking whether the Boost::Filesystem library is available… yes
    configure: error: Could not link against !
    ```
    *Fix*: You need to add the following parameters when running `configure`:
    ```bash
    --with-boost-system=lboost_system --with-boost-filesystem=lboost_filesystem
    ```

*   **Typical Error 2**:
    During `make`, you encounter:
    ```text
    undefined reference to 'boost::system::generic_category()'
    undefined reference to 'boost::system::system_category()'
    ```
    *Fix*: Once you have confirmed that the `boost::system` library exists and its path is correct, inspect the GCC link command (according to the make output):
    ```bash
    g++ -Wall -O3 -L/usr/local/lib/ -lboost_system -lboost_filesystem -o scribed store.o store_queue.o conf.o file.o conn_pool.o scribe_server.o network_dynamic_config.o dynamic_bucket_updater.o env_default.o -L/usr/local/lib -L/usr/local/lib -L/usr/local/lib -lfb303 -lthrift -lthriftnb -levent -lpthread libscribe.a libdynamicbucketupdater.a
    ```
    You need to move the `-lboost_system -lboost_filesystem` options to the very end of the command, and then manually execute the linking command inside the `src` directory to complete the compilation.

I ran into Error 1 myself. After trying out dozens of different ways, I finally got it resolved. The final successful `configure` parameters I used were:
```bash
./configure --config-cache --prefix=/usr/local --with-boost=/usr/local/lib --with-boost-system=boost_system --with-boost-filesystem=boost_filesystem CPPFLAGS="-DHAVE_INTTYPES_H -DHAVE_NETINET_IN_H -DBOOST_FILESYSTEM_VERSION=3"
```

---

### 4. References

1. http://www.2cto.com/os/201307/224832.html
2. http://abentotoro.blog.sohu.com/190515962.html
3. http://www.linuxidc.com/Linux/2012-12/76340.htm
4. http://shiyanjun.cn/archives/107.html
