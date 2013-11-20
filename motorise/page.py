# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
from tidylib import tidy_document

from form import Form
from link import Link

class Page(object):
    def __init__(self, url, response, body, code, agent):
        self.url      = url
        self.response = response
        self.body     = body
        self.code     = code
        self.agent    = agent

        self.tidy_doc = tidy_document(body)[0]
        self.bs4_doc  = BeautifulSoup(self.tidy_doc)

        self.cached_links = []

    def title(self):
        title_node = self.bs4_doc.select("title")[0].string

        if not title_node:
            return ""
        else:
            return title_node.strip()

    def status_code(self):
        return self.code

    def html(self):
        return self.body

    def select(self, css_selector):
        return self.bs4_doc.select(css_selector)

    def form(self, css_selector):
        return Form(self, self.bs4_doc.select(css_selector)[0])

    def submit(self, form):
        return self.agent.submit(form)

    def links(self):
        if len(self.cached_links) == 0:
            for selector in ['a', 'area']:
                for link in self.bs4_doc.select(selector):
                    self.cached_links.append(Link(link))

        return self.cached_links

    def find_link(self, **kwargs):
        for link in self.links():
            link_name = link.text().strip()
            link_href = link.href().strip()

            if 'name' in kwargs and link_name == kwargs['name']:
                return link

            if 'link' in kwargs and link_href == kwargs['link']:
                return link

            if 'name_regex' in kwargs and re.match(kwargs['name_regex'], link_name):
                return link

            if 'link_regex' in kwargs and re.match(kwargs['link_regex'], link_href):
                return link

        return None
