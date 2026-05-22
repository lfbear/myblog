---
layout: post
status: publish
published: true
title: "Docker in Practice: Demystifying Images & Containers"
lang: en
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
Understanding Docker's **images** and **containers** is often the very first hurdle for beginners. In this post, I'll share some of my hands-on insights to help newcomers wrap their heads around these concepts quickly.

*Note: This post is a quick-start guide to help beginners build intuition, not a deep academic dive into the inner workings of Docker. As such, some advanced details may be simplified or glossed over for clarity. For a more comprehensive look, I highly recommend checking out Daniel Eklund's illustrated guide: [Visualizing Docker Containers and Images](http://merrigrove.blogspot.hk/2015/10/visualizing-docker-containers-and-images.html), which is one of the main references for this post (you might need a VPN/proxy to access it).*

<!-- more -->

### 1. Image

Here is the official definition: An image is the foundation of a container. It is a read-only template that contains a set of layered filesystems stacked on top of each other, archiving **every filesystem change** on top of a base OS. An image does not have state and never changes.

> *Original:*
> *Docker images are the basis of containers. An Image is an ordered collection of root filesystem changes and the corresponding execution parameters for use within a container runtime. An image typically contains a union of layered filesystems stacked on top of each other. An image does not have state and it never changes.*

Personally, I like to compare it to a virtual machine (VM) image. When using a VM (whether in VirtualBox or VMware), you can export and share your configured system as a single file. That file is essentially an image. Of course, Docker images differ under the hood; they natively keep track of version histories, capturing every container `commit` and `save` inside their layers.

Think of it like onion layers: every time you perform a write operation and commit it, a new layer is wrapped around the outside. A common question among Docker beginners is: *"Why is my image size ballooning, and why doesn't running clean-up scripts reduce the size?"* The reason is that new layers are strictly additive. You are saving the *deltas* (changes) on top of the old state, not rewriting the final snapshot from scratch. While this makes your images larger, the huge benefit is that you can easily roll back to any previous state!

### 2. Container

Let's look at the official definition first: A container is a runtime instance of an image. It consists of the image, the execution environment, and a standard set of instructions. The concept is heavily borrowed from shipping containers, which standardized global transport. Docker containers define a **standard way to package and ship software**.

> *Original:*
> *A container is a runtime instance of a docker image.*
> *A Docker container consists of a Docker image, execution environment and standard set of instructions.*
> *The concept is borrowed from Shipping Containers, which define a standard to ship goods globally. Docker defines a standard to ship software.*

In my opinion, a container is just an active instance of an image—a dynamic, living runtime process. Think of it like instantiating an object (`new MyClass()`) in high-level programming languages.

However, keep in mind that containers are designed to be ephemeral—they can be destroyed or replaced at any moment. **Never** attempt to configure a stable, persistent service directly inside a running container (such services should be baked statically into the image so they spin up automatically when the container starts).

Furthermore, **never** store business or application data inside the container's own filesystem. Instead, use Docker volumes. That way, when the container is deleted, your data remains safely preserved on the host and can easily be attached to a replacement container.

### 3. How to Approach Images and Containers

Imagine you are writing a novel on your computer. When you finally finish a chapter, to make sure all your hard work is safe, you save the file. In Docker terms, this is when you should commit your container's state to a static image: you run `docker commit` and `save` it.

The next day, you get a burst of inspiration and want to keep writing. Here are your two paths:

*   **Path A (Computer stayed on, novel is still open in the editor)**: You jump back into your existing container (using `docker start` or `docker exec`).
*   **Path B (Computer was turned off, you boot up and open the file again)**: The temporary container is gone, so you spin up a brand new one from your saved image using `docker run`.

This analogy highlights the relationship between the dynamic runtime (container) and static storage (image). If you want to run your app, use a container; if you want to freeze the state and save it, build an image.

### 4. Converting Between Containers, Images, and Files

#### A. Container -> Image -> File (.tar)

*   **Exporting:** Container `--[commit]-->` Image `--[save]-->` `.tar` file
    *   *Commit:* `sudo docker commit [container_name] [image_name]`
    *   *Save:* `docker save -o [filename].tar [image_name]`
*   **Importing:** Container `<--[run]--` Image `<--[load]--` `.tar` file
    *   *Run:* `sudo docker run -t -i [image_name] /bin/bash`
    *   *Load:* `sudo docker load < [filename].tar`

#### B. Container -> File -> Image

*   Container `--[export]-->` `.tar` file `--[import]-->` Image
    *   *Export:* `sudo docker export [container_id_or_name] > [filename].tar`
    *   *Import:* `cat [filename].tar | sudo docker import - [image_name]`

### References

1.  **Visualizing Docker Containers and Images**: [http://merrigrove.blogspot.hk/2015/10/visualizing-docker-containers-and-images.html](http://merrigrove.blogspot.hk/2015/10/visualizing-docker-containers-and-images.html)
2.  **Docker Official Documentation**: [https://docs.docker.com/](https://docs.docker.com/)
3.  **Docker - From Beginner to Practice (Chinese)**: [http://dockerpool.com/static/books/docker_practice/index.html](http://dockerpool.com/static/books/docker_practice/index.html)
