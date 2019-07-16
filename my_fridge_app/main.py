# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import os
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        mango = {
            "name": "mangos",
            "amount": 500,
            "type": "fruit",
            "lethal_dose": 600
        }

        pineapple = {
            "name": "pineapple",
            "amount": 25,
            "type": "fruit",
            "lethal_dose": 20
        }

        grape = {
            "name": "grape",
            "amount": 10000,
            "type": "fruit",
            "lethal_dose": 100
        }

        all_food = [mango, pineapple, grape]

        values = {
            "food": mango,
            "all_food": all_food
        }
        template = JINJA_ENVIRONMENT.get_template("templates/index.html")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render(values))


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
