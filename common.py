
# -*- coding: utf-8 -*-

# Copyright 2017 Jakub Kukiełka

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import click
from flask import Flask, render_template, send_from_directory, Response
from flask_cors import CORS
from glob import glob

from stylus import Stylus
c_stylus = Stylus()
#c_stylus.use("nib")

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='[%',
        block_end_string='%]',
        variable_start_string='[[',
        variable_end_string=']]',
        comment_start_string='[#',
        comment_end_string='#]',
    ))

options = {
    'protocol': ''
}

app = Flask(__name__)
app.jinja_env.add_extension("pypugjs.ext.jinja.PyPugJSExtension")

# Enable CORS (cross-origin) between subdomains
CORS(app)

if app.debug:
    import serve.debug
    app.config['SERVER_NAME'] = 'argarak.dev:5000'
else:
    app.config['SERVER_NAME'] = 'argarak.me'

# The order at which stylesheets are loaded does not matter, so glob all
# stylesheets including subdirectories
_common_styles = glob(os.path.join(app.static_folder,
                                   "css", "common") + "/**/*.css",
                      recursive=True)

# Only select user scripts since the order at which they are loaded does
# not matter as much as external libraries
_common_scripts = glob(os.path.join(app.static_folder,
                                    "js", "common") + "/*.js")

# The order external libraries are loaded is important and so it cannot
# be part of the glob
_ext_scripts = [
    "vue.js",
    "vue-router.js",
    "vue-material.js"
]

_ext_scripts = ["%s" % (os.path.join(app.static_folder, "js", "common",
                                     "ext") + "/" + i,)
                for i in _ext_scripts]

_common_scripts = _ext_scripts + _common_scripts

_common_stylus = glob(os.path.join(app.static_folder, "css",
                                   "common") + "/**/*.styl",
                      recursive=True)

_common_styles += ["%s" % (os.path.splitext(i)[0] + ".css",)
                   for i in _common_stylus]

# Intercepts calls to css files to see if any of them are really stylus
# files. If it is a stylus file (.styl) then we compile it and return
# the compiled version as if it was in css in the first place.
@app.route("/css/<path:path>.css")
def compile_to_css(path):
    for i in _common_stylus:
        # Removes the path before and including /static, i.e. removes
        # irrelevant (in this case) directory information such as the
        # specific path in the system (e.g. /home/user/argarak.me...)
        split_i = i.split("/static")[1]

        # os.path.splitext allows us to split a path into a list where
        # the first item is the string before the file extension and
        # the second item being the extension itself.
        #
        # e.g. "/static/img/cat.jpg" becomes
        # ["/static/img/cat", ".jpg"]
        splitext_i = os.path.splitext(split_i)

        # "/css/" has to be added to the path string as `path` is
        # just the path after /css/ and so we must add it to
        # compare this successfully to splitext_i which does
        # include /css/. `path` also does not include the file
        # extension (.css) because that's how it finds out
        # whether it is a css file or not.
        if "/css/" + path == splitext_i[0]:
            # If the stylesheet is really a stylus file...
            if splitext_i[1] == ".styl":
                try:
                    # Open the stylus file (in the static directory)
                    with app.open_resource("static" + split_i) as f:
                        # Compile the stylus file after it's decoded
                        # into a regular str
                        compiled = c_stylus.compile(f.read().decode())
                        return Response(compiled, mimetype='text/css')

                except IOError as err:
                    print(err)

    return send_from_directory('static/css/' + path[:-len(
        path.split("/")[-1])], path.split("/")[-1] + ".css")

common_sources = {
    "styles":  ["%s" % (''.join((options["protocol"],
                                 "//",
                                 app.config["SERVER_NAME"],
                                 i.split("/static", 1)[1])),)
                for i in _common_styles],

    "scripts": ["%s" % (''.join((options["protocol"],
                                 "//",
                                 app.config["SERVER_NAME"],
                                 i.split("/static", 1)[1])),)
                for i in _common_scripts]
}

subdomain_list = [
    "blog",
    "archive",
    "dev",
]
