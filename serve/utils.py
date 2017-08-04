
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

from common import subdomain_list, app, options
from bs4 import BeautifulSoup as Soup

def lookup_favicon(subdomain=None):
    favicon_path = ''.join((options["protocol"],
                           "//",
                           app.config["SERVER_NAME"],
                           "/favicon/"))

    if subdomain == None:
        return favicon_path + "main.png?"

    if not subdomain in subdomain_list:
        return favicon_path + "invalid.png?"

    return favicon_path + subdomain + ".png?"

@app.template_filter()
def extract_head(html):
    soup = Soup(html, "html.parser")

    output = ""

    for child in soup.head.children:
        if str(child) != "\n":
            output += str(child)

    return output

@app.template_filter()
def extract_body(html):
    soup = Soup(html, "html.parser")

    output = ""

    for child in soup.body.children:
        if str(child) != "\n":
            output += str(child)

    return output

@app.template_filter("absolute")
def absolute_static_url(url):
    return ''.join((options["protocol"],
                    "//",
                    app.config["SERVER_NAME"],
                    url))
