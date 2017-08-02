
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
from flask import Flask, render_template
from glob import glob

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

app = Flask(__name__)
app.jinja_env.add_extension("pypugjs.ext.jinja.PyPugJSExtension")

if app.debug:
    import serve.debug
    app.config['SERVER_NAME'] = 'argarak.dev:5000'
else:
    app.config['SERVER_NAME'] = 'argarak.me'

# The order at which stylesheets are loaded does not matter, so glob all
# stylesheets including subdirectories
_common_styles = glob(os.path.join(app.static_folder, "css", "common") + "/**/*.css", recursive=True)

# Only select user scripts since the order at which they are loaded does
# not matter as much as external libraries
_common_scripts = glob(os.path.join(app.static_folder, "js", "common") + "/*.js")

# The order external libraries are loaded is important and so it cannot
# be part of the glob
_ext_scripts = [
    "vue.js",
    "vue-router.js",
    "vue-material.js"
]

_ext_scripts = ["%s" % (os.path.join(app.static_folder, "js", "common", "ext") + "/" + i,) for i in _ext_scripts]

_common_scripts = _ext_scripts + _common_scripts

print(_common_scripts)

common_sources = {
    "styles": ["%s" % ("//" + app.config["SERVER_NAME"] + i.split("/static", 1)[1],) for i in _common_styles],
    "scripts": ["%s" % ("//" + app.config["SERVER_NAME"] + i.split("/static", 1)[1],) for i in _common_scripts],
}

subdomain_list = [
    "blog",
    "archive",
    "dev",
]
