# -*- coding: utf-8 -*-

class Link(object):
    def __init__(self, node):
        self.node = node

    def text(self):
        return self.node.text

    def href(self):
        return self.node['href'] if self.node.has_attr('href') else ""

    def id(self):
        return self.node['id'] if self.node.has_attr('id') else ""
