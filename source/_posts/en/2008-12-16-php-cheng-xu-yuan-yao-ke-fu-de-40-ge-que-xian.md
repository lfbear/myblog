---
layout: post
status: publish
published: true
title: "Goodbye Rookie: 40 Signs You're Still a PHP Novice"
author:
  display_name: 小飞熊
  login: fbbear
  email: fbbear@sina.com
  url: 'https://lfbear.com'
author_login: fbbear
author_email: fbbear@sina.com
author_url: 'https://lfbear.com'
wordpress_id: 56
date: '2008-12-16 17:51:33 +0800'
date_gmt: '2008-12-16 09:51:33 +0800'
categories:
  - 程序人生
tags:
  - php
comments: []
abbrlink: 16717
lang: en
---
40 signs you are still a PHP novice.

<!--more-->

### Introduction
The English copyright of "40 Signs" belongs to Reinhold Weber, and the Chinese translation is by yangyang.

### Body
These signs are not meant to discourage you or brand you as a permanent amateur; their ultimate purpose is to show you how much more there is to learn.

Here are the 40 signs of a PHP novice:

1. **Failing to use tools like phpDoc to properly document your code.**  
*phpDoc is an excellent module under PEAR, similar to javadoc, used to generate API documentation from your code. Built with OOP principles, it scans PHP source files in a specified directory, parses dedicated tags in your comments, and generates XML (or other formats) along with indexes. Essentially, it builds documentation directly from your inline source comments.*

2. **Ignoring excellent IDEs like Zend Studio or Eclipse PDT.**  
*I don't quite know how to describe Zend, but under the cover of night, someone once said: Zend is to the PHP world what Microsoft is to the software world. Eclipse is another versatile IDE that most people use for Java, but PDT (PHP Development Tools) is a plugin that lets you write PHP in Eclipse. If you're interested, you can even write your own plugin for Eclipse.*

3. **Never using any form of version control system, such as Subclipse.**  
*Version control? Let's understand version control first: it's basically a data repository that tracks every change you make to your files. Once you get that, understanding a VCS is simple. A deeper dive is too long to fit here, so I'll just recommend looking into it and choosing one for yourself!*  
*(1) [Link 1](http://www.phpchina.com/bbs/thread-43236-1-1.html)*  
*(2) [Link 2](http://www.phpchina.com/bbs/thread-46209-1-1.html)*

4. **Failing to adopt coding/naming standards and common conventions, or failing to stick to them throughout the project life cycle.**  
*I think good code formatting habits are incredibly satisfying. Indentation is absolutely essential—otherwise, staring at a dense, aesthetic-free block of text is just depressing. Generally, indentation should be 4 spaces; the PEAR standard discourages using tabs because they can cause issues in certain environments. For naming variables, I recommend camelCase (e.g., `myName`), and for class names, PascalCase (e.g., `MyName` or `My_Name`). As for underscores, I don't think they make a huge difference.*

5. **Failing to use a unified development methodology.**  
*Here are a few recommended articles:*  
*(1) [Link 1](http://www.phpchina.com/html/42/1142-7314.html)*  
*(2) [Link 2](http://www.ibm.com/developerworks/cn/web/wa-jacquard/index.html#N10064)*

6. **Failing to sanitize (or validate) inputs or SQL query strings.**  
*Always remember one core principle: never trust raw user input. Filtering user inputs is the bedrock of Web security. A designer should always know where data comes from, filter it diligently, and strictly separate sanitized data from untrusted raw data.*

7. **Failing to thoroughly plan your program before coding.**  
*Personally, I feel this is just like drawing flowcharts before writing code or outlining a project's dev pipeline. It shouldn't need much explanation.*

8. **Failing to use Test-Driven Development (TDD).**  
*Test-Driven Development (TDD) is an essential component of Extreme Programming. Its core philosophy is to write tests before you write functional code. That is, once a feature is defined, you first think about how to test it, write the tests, and then write the code to satisfy those tests. This cycle is repeated for every feature until development is complete. "Clean code that works" is the ultimate goal of TDD.*

9. **Failing to code and test with error reporting turned on.**  
*I assume most people enable error reporting while coding. As a quick reference, `error_reporting()` takes an optional error level argument and sets which errors should be displayed. For details, see: [PHP Manual](http://cn2.php.net/manual/en/function.error-reporting.php)*

10. **Ignoring the benefits of a debugger.**  
*A few debugger recommendations:*  
*(1) Zend IDE*  
*(2) APD*  
*(3) Xdebug*

11. **Failing to refactor your code.**  
*Refactoring means adjusting the internal structure of software without changing its "observable behavior," using a series of refactoring techniques. The goal is to make the software easier to understand and cheaper to modify without breaking external functionality. Refactoring improves software design, helps developers spot bugs, and speeds up development. In short, refactoring is improving the design of existing code.*

12. **Failing to use MVC-like patterns to separate application layers.**  
*MVC (Model-View-Controller) splits an application: the View is the user interface, the Model handles the core business logic and tasks, and the Controller manages the mapping between the two, routing user actions to the right Model and returning the corresponding View.*

13. **Failing to understand these concepts: KISS, DRY, MVC, OOP, REST.**  
*(1) **KISS** stands for "Keep It Simple, Stupid," advocating for simplicity in design and avoiding unnecessary complexity.*  
*(2) **DRY** stands for "Don't Repeat Yourself," emphasizing the avoidance of duplicate code to prevent bugs, complexity, and maintenance headaches.*  
*(3) **OOP** (Object-Oriented Programming): I love the classic car analogy here. A "Car" is a Class, which has attributes like wheels, chassis, and engine, and methods like accelerate and brake. A "Rolls-Royce" is an Object instantiated from that Class, inheriting its attributes and methods. How are acceleration and braking actually implemented? That information is hidden—which is "Encapsulation"—leaving only the user interface (the pedals) for us to interact with. As for "Polymorphism," a crude analogy is a vending machine: you use the same method—inserting coins—but inserting $2 vs. $5 yields completely different results (unless the machine is broken, of course).*  
*(4) **REST** (Representational State Transfer) is an architectural style for designing networked applications, lowering complexity and improving scalability. It outlines key principles:*  
&nbsp;&nbsp;&nbsp;&nbsp;*a. Everything on the web is abstracted as a resource;*  
&nbsp;&nbsp;&nbsp;&nbsp;*b. Every resource is mapped to a unique resource identifier;*  
&nbsp;&nbsp;&nbsp;&nbsp;*c. Resources are manipulated through generic connector interfaces;*  
&nbsp;&nbsp;&nbsp;&nbsp;*d. Operations on resources do not alter their identifier;*  
&nbsp;&nbsp;&nbsp;&nbsp;*e. All operations are stateless.*

14. **Directly outputting content (via echo/print) inside functions or classes instead of using return.**  
*Whenever I study code written by senior developers, they always use return. So I just followed suit because it felt cleaner and more disciplined. Honestly, I'm a bit confused by this rule myself—functions generally need a return statement anyway, unless they are specifically built as output helpers.*

15. **Ignoring the advantages of unit testing or general testing.**  
*(1) **Unit Testing** is the lowest level of testing in software development. Individual units of code are tested in isolation from the rest of the application, which keeps projects on track and refines design. I remember when I used to write long C programs, I'd always append some test code at the end of key modules to verify them. I wonder if that counts as unit testing! ^_*  
*(2) **General Testing Techniques**: This reminds me of a book from the Turing Series I saw in the library, something like "Software Testing...", though I forgot the exact title. These all fall under the software testing umbrella. If you're interested, you can download some materials here: [Link](http://bbs.phpchina.com/thread-94241-1-1.html)*

16. **Always returning hardcoded HTML instead of returning raw data, strings, or objects.**

17. **Always hardcoding messages and configuration parameters.**  
*Hardcoding makes programs incredibly rigid, leading to maintenance nightmares and occasionally compilation issues down the line.*  
*Let's do a quick deep dive:*  
*In programming, "hardcoding" refers to embedding fixed values directly instead of using variables. Once compiled, changing these values becomes extremely difficult. In most languages, you can define a constant or configuration key to represent a value. If you need to change it, you change it in one place and recompile, and the change propagates everywhere. While you could technically use find-and-replace in an editor, it's highly error-prone—and in software, even a tiny typo can be unforgiving. The best practice is to separate your configuration into a dedicated space. As a general rule, hardcoding should be strictly avoided.*  
*(Note: Sometimes people jokingly use "hardcode" to refer to low-level, difficult languages like C or C++, while using "softcode" to describe easy languages like VB.)*

18. **Failing to optimize your SQL queries.**  
*SQL query optimization involves transforming poorly performing SQL statements into highly efficient ones with the exact same output. The benefits are obvious, and today you can even use automated AI tools to help optimize SQL.*

19. **Failing to use `__autoload`.**  
*The `__autoload` magic function is automatically triggered when attempting to instantiate a class that hasn't been defined yet. This gives the scripting engine one last chance to load the required class file before PHP throws a fatal error.*  
*For details, see: [PHP Manual](http://cn.php.net/manual/zh/language.oop5.autoload.php)*

20. **Not implementing intelligent error handling (e.g., PEAR's ErrorStack).**  
*PEAR_ErrorStack provides a stack-based error handling framework. It unifies error handling across different modules into a single, centralized location, making it easier to integrate independent packages into the same application. (Translated from: [PEAR](http://pear.php.net/package/PEAR_ErrorStack))*

21. **Using `$_GET` instead of `$_POST` for destructive state-changing actions.**  
*For sensitive operations, using `$_GET` exposes critical information directly in the browser's URL bar.*

22. **Not knowing how to utilize Regular Expressions.**  
*Regex? Don't worry if you don't know it yet—it's never too late to learn: [Regex Tutorial](http://bbs.phpchina.com/thread-89223-1-1.html)*

23. **Never having heard of SQL Injection or Cross-Site Scripting (XSS).**  
*(1) **SQL Injection (SQLi)** involves inserting malicious SQL commands into web forms, input fields, or URL query strings to trick the server into executing them. For instance, in the past, many movie websites leaked VIP passwords because their query forms were vulnerable to SQLi attacks.*  
*(2) **Cross-Site Scripting (XSS)** is defined in the industry as: "An attacker injecting malicious script code into a trusted website's HTML." Because HTML allows interactive scripting, attackers can inject malicious tags to steal user data, like forum session cookies. Since cookies often store session details or credentials, this compromises security. A simple JS snippet like `alert(document.cookie)` can instantly display a user's cookie. Attackers use this to silently send your sensitive cookies to their logging servers.*

24. **Failing to support simple configuration, refusing to pass arguments to class constructors for set/get initialization, or ignoring runtime constants.**  
*Put simply: always allow your class constructors to accept parameters!*

25. **Failing to understand the advantages and disadvantages of Object-Oriented Programming (OOP).**

26. **Abusing OOP regardless of project size.**

27. **Believing that reusable software must be written using OOP.**  
*OOP Advantages: It brings code closer to the real world by mapping things to objects with properties and methods, making programming feel more intuitive and human-like.*  
*OOP Disadvantages: In low-level execution (like in C++), because it operates at a higher logical abstraction layer, it often requires sacrificing raw performance—which can sometimes be critical.*

28. **Failing to leverage intelligent default values.**  
*I think using sensible defaults is just a great habit.*

29. **Lacking a single configuration file.**  
*Having a dedicated `config.php` is absolutely a must-have in my book.*

30. **Using a `.inc` extension instead of `.php` to hide source files.**  
*`.inc` stands for "include file." People historically used it to show a file's purpose, somewhat similar to `.h` or `.hpp` header files in C/C++. Using `.inc` files can make code more readable and easier to maintain—but if they aren't parsed as PHP by the server, their raw source code will be exposed to anyone who visits the URL! (So always use `.inc.php` or hide them outside the public web root).*

31. **Failing to use a database abstraction layer.**  
*Please refer to this thread: [DB Abstraction Layer](http://bbs.phpchina.com/thread-94258-1-1.html)*

32. **Failing to stay DRY (see point 13). If you are constantly copy-pasting code, it means your architecture is poorly designed.**

33. **Failing to design functions/classes/methods that do just one thing, or failing to combine them modularly.**  
*This takes practice. You have to learn and refine this through real-world experience.*

34. **Failing to leverage the core strengths of OOP, such as abstract classes, interfaces, polymorphism, inheritance, and access modifiers (public, private, protected).**  
*Oh my god, I think we should just refer to points 25–27. This is another area where you grow through practice.*

35. **Failing to optimize your software architecture with existing design patterns.**  
*I highly recommend reading "Head First Design Patterns".*

36. **Failing to let users (developers) define a base directory when dealing with a large volume of files or folders.**  
*Once an app goes live, it generates logs, and subsequent updates can make directories messy. A great practice is to define all paths in a single config file, allowing developers to change them easily so the system stays clean and organized.*

37. **Polluting the namespace—for instance, by naming your library functions with overly common strings.**  
*Sigh, this is indeed a bad habit, but good habits are built over time!*

38. **Failing to use table prefixes when designing database tables.**  
*I think PHPChina, for example, uses prefixes like `ppc_` or `pcc_`. It definitely has its benefits. It's similar to naming fields with a type prefix, like `txtUsername`.*

39. **Failing to use a unified template engine.**  
*No one wants their website pages to load sluggishly in a user's browser, so development teams generally standardize on a unified template engine.*

40. **Ignoring existing PHP frameworks and being too lazy to explore them; after all, advanced development philosophies and beautiful code are often found within them.**  
*Examples include Zend Framework, CakePHP, FleaPHP, ThinkPHP, etc.*  

*Compiled from the internet. Huge thanks to the original author and translators for their hard work!*
