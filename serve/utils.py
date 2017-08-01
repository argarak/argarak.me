
from common import subdomain_list, app
from bs4 import BeautifulSoup as Soup

def lookup_favicon(subdomain=None):
    favicon_path = "//" + app.config["SERVER_NAME"] + "/favicon/"

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
