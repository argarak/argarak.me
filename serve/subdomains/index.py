
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

from common import app, common_sources, navbar
from flask import render_template
from flask_classy import FlaskView
from serve.utils import lookup_favicon

from os import path

class MainView(FlaskView):
    route_base = "/"
    subdomain = None

    def generate_tabs(self, navbar):
        self.tabs = navbar
        i = 0

        for tab in self.tabs:
            with open(path.join(app.static_folder, "icon", tab["filename"]), "r") as f:
                self.tabs[i]["svgData"] = f.read()
            self.tabs[i]["index"] = i
            self.tabs[i]["aburl"] = "/" + tab["url"]
            i += 1

    def __init__(self):
        self.subdomain = None
        self.template = "index.pug"

        self.sources = common_sources

        #self.sources["styles"].extend([])
        #self.sources["scripts"].extend([])

        self.meta = {
            "title": "main",
            "current_favicon": lookup_favicon(self.subdomain),
            "default_tags": "a, b, c, d",
            "description": "a test!",
            "is_article": False
        }

        self.generate_tabs(navbar)

    def index(self):
        return render_template(self.template,
                               sources=self.sources,
                               meta=self.meta,
                               tabs=self.tabs)

MainView.register(app)
