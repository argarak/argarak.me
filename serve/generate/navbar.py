
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
from config import config
from bs4 import BeautifulSoup as Soup
from serve.generate.data import data

import json
import glob

filename = "navbar.json"
icon_path = ''.join((app.static_folder, "/icon/"))

def navbar():
    icon_data = {}

    print(icon_path + "*.svg")

    for i, val in enumerate(config["navbar"]):
        print(i)
        try:
            with open(icon_path + val["filename"]) as f:
                soup = Soup(f.read())
                colour = ""

                for element in soup.find_all(["svg", "path", "circle", "g"]):
                    fill_colour = element.get("fill")

                    if fill_colour != None and fill_colour != "none":
                        colour = fill_colour

                if not colour:
                    for element in soup.find_all(["svg", "path",
                                                  "circle", "g"]):
                        stroke_colour = element.get("stroke")

                        if stroke_colour != None and stroke_colour != "none":
                            colour = stroke_colour

                icon_data[val["filename"]] = colour

        except IOError as err:
            print(err)

    return json.dumps(icon_data)

data[filename] = navbar
