# -*- coding: utf-8 -*-

import urllib3
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from .page import Page

class Agent(object):
    def __init__(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.session = requests.Session()

    def get(self, url, **kwargs):
        response = self.session.get(url, **kwargs)

        return Page(url, response, response.text, response.status_code, self)

    def submit(self, form, **kwargs):
        if form.method.lower() == "get":
            response = self.session.get(form.action, params=form.fields, **kwargs)
        else:
            response = self.session.post(form.action, data=form.fields, **kwargs)

        return Page(form.action, response, response.text, response.status_code, self)
