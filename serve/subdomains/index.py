
from common import app, common_sources
from flask import render_template
from flask_classy import FlaskView
from serve.utils import lookup_favicon

class MainView(FlaskView):
    route_base = "/"
    subdomain = None

    def __init__(self):
        self.subdomain = None
        self.template = "index.pug"

        self.sources = common_sources

        print(self.sources)

        #self.sources["styles"].extend([])
        #self.sources["scripts"].extend([])

        self.meta = {
            "title": "main",
            "current_favicon": lookup_favicon(self.subdomain),
            "default_tags": "a, b, c, d",
            "description": "a test!",
            "is_article": False
        }

    def index(self):
        return render_template(self.template, sources=self.sources, meta=self.meta)

MainView.register(app)
