---
title: What’s new in Version 3
author: Argarak
date: 14 September 2016
template: article.jade
tags: Nexus
---

As you might have noticed, version 3 of the Argarak’s Nexus blog has been released! Some fairly standard user-interface changes have occurred, which you may have already noticed. This includes...

## General

* A new landing page with automatically scrolling blog articles, including transitions. (The colours on the panel don’t really mean anything - they’re randomly selected and generally only used for aesthetic);
* Slightly darker background - #111111 to #0e0e0e;
* No annoying cookies and licensing pop-up - now the licensing information is stored on the top of each article and is displayed with the use of a modal;*
* Super responsive - should work on any device with a half-decent browser;
* On medium sized devices, the pop-up sidebar has been removed, instead being replaced by a bottom navigation toolbar. I’ve changed this since I’ve read that it’s not [user engaging.](http://thenextweb.com/dd/2014/04/08/ux-designers-side-drawer-navigation-costing-half-user-engagement/);
* Pink and red colour-scheme;
* Thicker Nexus Logo;
* JavaScript disabled message;
* Pink text highlight.

## About, Archive pages

* Bold, red title headers in the Archive and About pages;
* Robust `base32`{class="inline"} email munging protection

## Blog page

* A search bar! Took a while, but will eventually be an effective filter method when I make more blog posts (which will take a while obviously);
* Tag filter support, categorises all blog posts.

## Programs page

* Material pre-loader;
* Material-style list of all my current repositories which respond to the click and redirect you to the appropriate repository page on GitHub.

## Micro-blogging page

* Now I can post quick and short updates and stuffs with the use of a remote [pump.io](https://pumpyourself.com/) server (publishing the posts with a program called [`p`{class="inline"}](https://github.com/xray7224/p)); 
* Pre-loader again, this time it’s more important as my bodged method of collecting all the posts may take a while;
* Displays author, date, description and permalink.

Not much at all was changed about the Archive (other than the title) or RSS page.

*\*If you were wondering the cookies were to actually preserve the pop-up while you were browsing other pages - however, this was not an permanent cookie and it would be erased after you would close the browser. That was the only thing the cookies were used for. I don’t really know why I was showing this pop-up to be honest, as the cookie law does not affect me, and I could have just mentioned the license info. somewhere else on the site.*

# What's up with those version names?!

Those are just codenames I come up with on the spot really. They usually have quite a shallow meaning. For instance;

* Version 3 - Angled Ink-Pug refers to Angled = Angular, Ink = Stylus CSS pre-processor and Pug refers to the HTML pre-processor (and no I’ve not changed the `.jade`{class="inline"} files to `.pug`{class="inline"} yet)
* Version 2.11 Paper Feather (one that was not published) - Feather because I cut 50 megabytes from stored video files in the history and Paper because I wanted the version to comply more with material design (~~I’ll~~ <a ui-sref="blog({ name: '', title: ''})">I won’t get onto that...</a>
 )
    
Sometimes version names have no meaning at all, such as version 2 - Horse Radish. 
