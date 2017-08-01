
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

        print(self.sources)

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
