
from common import app, common_sources
from serve.subdomains.index import MainView
from serve.utils import lookup_favicon

class BlogView(MainView):
    route_base = "/"
    subdomain = "blog"

    def __init__(self):
        self.subdomain = "blog"
        self.template = "blog.pug"
        self.sources = common_sources

        print(self.sources)

        self.meta = {
            "title": "blog",
            "current_favicon": lookup_favicon(self.subdomain),
            "default_tags": "a, b, c, d",
            "description": "a test!",
            "is_article": False
        }

BlogView.register(app)
