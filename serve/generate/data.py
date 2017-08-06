
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

import os
from common import app
from flask import Response

data = {}

@app.route("/data/<data_file>")
def serve_data(data_file):
    for key in data:
        if data_file == key:
            if os.path.splitext(data_file)[1] == ".json":
                return Response(data[key](), mimetype='application/json')
            return data[key]()
