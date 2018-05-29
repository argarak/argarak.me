
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

from common import app
from serve.generate.data import data

from bs4 import BeautifulSoup as Soup
from glob import glob
from os import path
import frontmatter
import pypandoc
import json

filename = "articles.json"

def articles():
    article_list = glob(path.join(app.static_folder, "articles") + "/*")
    article_data = []

    for val in article_list:
        article = {}

        with open(val + '/index.md') as f:
            post = frontmatter.load(f)

            if not "title" in post.metadata:
                console.log("Warning: no title in post, skipping.")
                continue

            article["title"] = post["title"]

            if "author" in post.metadata:
                article["author"] = post["author"]
            else:
                article["author"] = "None"

            if "tags" in post.metadata:
                article["tags"] = post["tags"]
            else:
                article["tags"] = "None"

            if "date" in post.metadata:
                article["date"] = post["date"]
            else:
                article["date"] = ""

            output = pypandoc.convert_text(post.content, "html",
                                           extra_args=["--standalone"],
                                           format="md")

            
            soup = Soup(output, "html.parser")
            first_paragraph = soup.find("body").find("p")

            if not first_paragraph:
                article["intro"] = "None"
            else:
                article["intro"] = first_paragraph.get_text()

            article_data.append(article)

    return json.dumps({
        "articles": article_data
    })

data[filename] = articles
