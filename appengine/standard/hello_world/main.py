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
from twilio import twiml
import json
import urllib
import urllib2
import os
import random
import time

auth_token=''

class CallHandler(webapp2.RequestHandler):
    def post(self):
        sid = self.request.params.get('sid')
        self.response.headers['Content-Type'] = 'application/xml'
        resp = twiml.Response()
        resp.say("How can I help you")
        resp.record(action="http://tweek65apiioapp.appspot.com/actionurl", method="POST", maxLength="20")
        self.response.write(str(resp))

class ActionURL(webapp2.RequestHandler):
    def post(self):
        j = json.loads(self.request.body)
        result = j['result']

        #request = urllib2.Request("https://api.api.ai/v1/intents?v=20150910", None, {"Authorization": "Bearer %s" %auth_token})
        #response = urllib2.urlopen(req)
        #html=response.read()
        #json_obj=json.loads(html)

        self.response.headers['Content-Type'] = 'application/xml'
        resp = twiml.Response()
        resp.say("Hello world")
        self.response.write(str(resp))

app = webapp2.WSGIApplication([
    ('/incomingcall', CallHandler),
    ('/actionurl', ActionURL),
], debug=True)
