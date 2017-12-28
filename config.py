
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

config = {
    "debug_domain": "argarak.dev:5000",
    "domain": "argarak.me",

    "subdirectories": [
        "",
        "about",
        "blog",
        "dev",
        "archive",
        "microblog",
        "rss"
    ],

    # HTTP/HTTPS
    "protocol": "",

    # Sets the order the navbar will be
    "navbar": [
        {
            "filename": "nexus.svg",
            "url": "",
            "tooltip": "Home"
        },
        {
            "filename": "about.svg",
            "url": "",
            "tooltip": "About"
        },
        {
            "filename": "blog.svg",
            "url": "",
            "tooltip": "Blog"
        },
        {
            "filename": "programs.svg",
            "url": "",
            "tooltip": "Programs"
        },
        {
            "filename": "archive.svg",
            "url": "",
            "tooltip": "Archive"
        },
        {
            "filename": "microblog.svg",
            "url": "",
            "tooltip": "Microblog"
        },
        {
            "filename": "rss.svg",
            "url": "",
            "tooltip": "RSS"
        }
    ]
}
