# -*- coding: utf-8 -*-

import requests

from page import Page

class Agent(object):
    def __init__(self):
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
