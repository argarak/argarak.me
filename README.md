**old version: see newdev branch**

# argarak.me
New website under different back-end.

## Details

This website will be hosted on the [argarak.me](http://argarak.me/) domain under [Scaleway](https://www.scaleway.com/) with a Debian system running [nginx](http://nginx.org/).

The overall infrastructure is still under consideration however currently I’m looking at running this website with:

* Python back-end with [Flask](http://flask.pocoo.org/).

* Custom comments and microblogging storage system.

* ~~Switching frameworks from [angular.js v1.-](https://angularjs.org/) to [vue.js](https://github.com/vuejs/vue) and [angular material](https://material.angularjs.org/latest/) to [vue-material](https://github.com/vuematerial/vue-material). This will help me create a cleaner and more maintainable structure to my code and also for longer-term reasons, since angular v1.- will become deprecated at some point and I don't want to use angular v2 due to poor documentation, poor ECMAScript 5 support, Typescript and confusing structure.~~

* Pure vanilla javascript!

* No longer using [wintersmith](http://wintersmith.io/) because the website is no longer statically generated and running my own scripts to take care of markdown, templating etc.

* Deploying a WSGI-based server such as [Gunicorn](http://gunicorn.org) alongside nginx on a Debian server.

## Running in development mode

To start a debug flask server, use the `nexus` script like so:

`./nexus -d run`

## What's going to happen to `argarak.github.io`?

The original source code for that website will still be here for archival purposes but `argarak.github.io` will redirect to `argarak.me`. All the old blog posts will be available on the new website however they'll all be under one post or in the archives as most of the content there only applies to that version of the website which might make things confusing.
