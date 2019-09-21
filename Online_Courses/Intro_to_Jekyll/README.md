# Overview of Jekyll
Jekyll is a framework that transforms your plain texts into static website without needing to knowing HTML/CSS/Javascript. However, if you do know programming, you can use Jekyll and implement new features. 

*Follow the steps below in order.*

**Downloading the Programs**

To use Jekyll, you need to install 2 things:
1. Ruby, a programming language Jekyll was built with.
2. RubyGems, a package manager for Ruby that allows us to use, update, install (eg. Jekyll), and maintain Ruby programs.

To install Ruby & RubyGems:
1. Search for "Terminal" or "iTerm" in the Launchpad/Searcg button on your MAC computer. Open the program.
2. Type: `ruby -v`. Press enter. You will see something like: ruby 2.3.3. You will need a ruby version 2.1.x or higher. 
3. Type: `gem -v`. Press enter. If you have gem installed, you will see something like: gem 2.5.2.

To install Jekyll:
1. In the terminal, type: `gem install jekyll bundler`. Thee RubyGems package manager "gem" installs Jekyll.

**Creating a Basic Website**

To create a Jekyll website:
1. Write `jekyll new website_name`. This will create files within `website_name` folder.
2. Move into the directory by typing: `cd website_name`.
3. To see the website in your web browser, type: `bundle exec jekyll serve`. You only need to type bundle exec once. This will start a website on the local host address (eg. http://127.0.0.1.4000). A new web browser will open with local host 4000.
4. Open the web browser and you will see localhost: 4000 in the url.

To understand the different folders within website_name:
**posts:** where all your blog posts will be stored
**site:** where the main website code is stored; automatically updated. This holds the finished version of your website
**config.yml:** attributes about the site (eg. title, email, url, etc.)
**Gemfile:** file used with Ruby. Stores dependencies (eg. jekyll, minima -- minima is the website's them)

**Creating a post: Front matter**

Front matter is information we store about the pages of the website (eg. title, date, author, etc.). The information in blogpost files are written in MarkDown.
  1. Move into the _posts_ directory by typing: `cd _posts`.
  2. View the only file in the directory by typing: `vim file_name`.
  
At the top of the file, you will see '---' (3 dashes) followed by text and another 3 dashes. This is the front matter that provides information about the post. Front matter could be written in two languages: YAML or JSON. See below for an example:
```
---
layout: post
title: "Welcome to MedInnovator!"
date: 2019-09-20 15:48:49 -0700
categories: jekyll blogs
author: "Victoria Nguyen"
---
```
All the pages need Front matter.

**Customizing the Website**


## Citatons & Additional Resources
-[Mike Dane's Bite-sized Intro to Jekyll](https://www.youtube.com/watch?v=T1itpPvFWHI&list=PLLAZ4kZ9dFpOPV5C5Ay0pHaa0RJFhcmcB)
