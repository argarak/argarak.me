
from common import subdomain_list, app

def lookup_favicon(subdomain=None):
    favicon_path = "//" + app.config["SERVER_NAME"] + "/favicon/"

    if subdomain == None:
        return favicon_path + "main.png"

    if not subdomain in subdomain_list:
        return favicon_path + "invalid.png"

    return favicon_path + subdomain + ".png"
