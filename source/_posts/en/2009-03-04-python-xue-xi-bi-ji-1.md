---
layout: post
status: publish
published: true
title: "Python Basics: Datatypes and Key Functions"
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
lang: en
---
An introductory guide covering Python's basic data types and essential functions.

<!--more-->

### 1. Data Types

---

#### a. Dictionary (`dict`)

*   **Definition**:
    `d = {key1: value1, key2: value2, ...}`
    Defined using curly braces `{}`. Key-value pairs are separated by colons `:`, and multiple elements are separated by commas `,`.
*   **Constraints**:
    *   Keys must be unique and are case-sensitive. Assigning a value to an existing key will overwrite the old value.
    *   Dictionary elements are unordered.
    *   Values can be of any data type.
*   **Operations**:
    *   *Assignment*: `d['newkey'] = newvalue`
    *   *Delete an element*: `del d['newkey']`
    *   *Clear dictionary*: `d.clear()`

---

#### b. List (`list`)

*   **Definition** (think of it as a dynamic array):
    `l = [a, b, c, ...]`
    Defined using square brackets `[]`, with elements separated by commas `,`.
*   **Constraints**:
    *   Elements are ordered.
    *   For a non-empty list, the first element is `l[0]`. In a list with `n` elements, the last element is `l[n-1]` (or `l[-1]`).
    *   Lists allow negative indexing. Negative values count backward from the end of the list.
    *   Values can be of any data type.
*   **Slicing**:
    Specify two index values to get a subset: `l[0:3]` returns the first 3 elements of the list. The start and end indexes can be omitted, defaulting to `0` and `-1` respectively.
*   **Operations**:
    *   *Add*:
        *   `l.append('new')`: Appends an element to the end of the list.
        *   `l.insert(1, 'new')`: Inserts an element at a specified index. Elements after it will shift one position to the right.
        *   `l.extend(["two", "elements"])`: Concatenates two lists. Note that the argument for `extend` must be a list, and new elements are added to the end.
    *   *Search*:
        *   `l.index('a')`: Finds the first occurrence of a value in the list and returns its index. If the value is not found, Python raises an exception.
        *   `'a' in l`: Tests if a value is in the list. Returns `True` if it exists, otherwise `False`.
    *   *Delete*:
        *   `l.remove('a')`: Removes the first occurrence of the value.
        *   `l.pop()`: Removes and returns the last element of the list.
    *   *List Operators*:
        *   `+`: Concatenates lists (similar to `extend`, though `extend` is faster for large lists).
        *   `*`: Repeats the list a specified number of times.

---

#### c. Tuple (`tuple`)

A tuple is simply an immutable list.
*   **Definition**:
    `t = ('a', 'b', 'c')`
    Defined using parentheses `()`, with elements separated by commas `,`.
*   **Constraints**:
    *   You cannot add, remove, or modify elements in a tuple.
*   **Advantages**:
    *   Tuples are faster than lists; perfect for constant values.
    *   Safer. You can easily convert a tuple to a list (but not vice versa, as lists are mutable).
    *   Can be used as dictionary keys (lists cannot, because they are mutable).
    *   Tuples can be used for string formatting.

---

### 2. Function Definition

```python
def function(parameter1, parameter2, ...):
    # Function body requires indentation
```

#### Essential Built-in Functions

*   **type 函数**: Returns the data type of any object.
*   **str 函数**: Casts data into a string.
*   **dir 函数**: Returns a list of valid attributes and methods for an object.
*   **callable 函数**: Checks if an object is callable (e.g., a function or method).
*   **getattr 函数**: Retrieves a reference to an attribute/method by name; a core feature for reflection/introspection and dispatching.

#### Other Tips

*   Python's built-in functions reside in the `__builtin__` module.
*   *Recommended learning resource*: *Dive into Python*—an excellent book!
