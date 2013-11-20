# -*- coding: utf-8 -*-

import requests

from page import Page

class Agent(object):
    def __init__(self):
        self.session = requests.Session()

    def get(self, url):
        response = self.session.get(url)

        return Page(url, response, response.text, response.status_code, self)

    def submit(self, form):
        if form.method.lower() == "get":
            return self.session.get(form.action, data=form.fields)
        else:
            response = self.session.post(form.action, data=form.fields)

            return Page(form.action, response, response.text, response.status_code, self)
