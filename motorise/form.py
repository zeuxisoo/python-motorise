# -*- coding: utf-8 -*-

import re
import sys
import urlnorm

class Form(object):
    def __init__(self, page, form):
        self.page = page
        self.form = form

        self.action = self.form['action'] if self.form.has_attr('action') else page.url
        self.method = self.form['method'] if self.form.has_attr('method') else "get"
        self.name   = self.form['name']  if self.form.has_attr('name') else ""

        self.action = urlnorm.norm(self.page.url + self.action)

        self.fields = dict()
        self.load_hidden_fields()

    def load_hidden_fields(self):
        input_nodes = self.form.select("input[type=hidden]")

        for input_node in input_nodes:
            self.fields[input_node.get('name')] = input_node.get('value')

    def set_field(self, name, value):
        self.fields[name] = value

    def submit(self):
        return self.page.submit(self)
