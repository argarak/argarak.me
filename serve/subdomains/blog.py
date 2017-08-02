
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

from common import app, common_sources
from serve.subdomains.index import MainView
from serve.utils import lookup_favicon
from flask_classy import FlaskView

from flask import render_template
import pypandoc

from bs4 import BeautifulSoup as Soup

class BlogView(MainView):
    route_base = "/"
    subdomain = "blog"

    def __init__(self):
        self.subdomain = "blog"
        self.template = "blog.pug"
        self.article_template = "article.pug"

        self.sources = common_sources

        self.meta = {
            "title": "blog",
            "current_favicon": lookup_favicon(self.subdomain),
            "default_tags": "a, b, c, d",
            "description": "a test!",
            "is_article": False
        }

    def article(self, article_name):
        try:
            with app.open_resource("static/articles/" + article_name + "/index.md") as f:
                output = pypandoc.convert_text(f.read().decode(), "html",
                                               extra_args=["--standalone"], format="md")

                soup = Soup(output, "html.parser")

                title = soup.find('title')
                base = soup.new_tag('base')
                base['href'] = "//" + app.config["SERVER_NAME"] + "/articles/" + article_name + "/"
                title.insert_after(base)

                return render_template(self.article_template, html=str(soup),
                                       meta=None, sources=self.sources)

        except IOError as err:
            print(err)


BlogView.register(app)
