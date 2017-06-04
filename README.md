# argarak.me
New website under different back-end.

## Details

This website will be hosted on the [argarak.me](http://argarak.me/) domain under [DigitalOcean](https://m.do.co/c/82675aee4c5d) with a Debian system running [nginx](http://nginx.org/).

The overall infrastructure is still under consideration however currently I’m looking at running this website with:

* Python back-end with [Flask](http://flask.pocoo.org/).
* Storing comments and post data in [redis](https://redis.io/).
* Continuing to use [angular.js v1.-](https://angularjs.org/) and [angular material](https://material.angularjs.org/latest/) as it’s still the best material framework in my opinion.
* No longer using [wintersmith](http://wintersmith.io/) as it’s the website is no longer statically generated and development of it has become sporadic.
* Writing my own deployment and generation scripts via Flask and [click](http://click.pocoo.org/5/).
