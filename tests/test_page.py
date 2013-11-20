# -*- coding: utf-8 -*-

from .base_suite import BaseSuite
from motorise import Page, Form, Link
from bs4.element import Tag
from requests.models import Response

class TestPage(BaseSuite):
    def test_title(self):
        page  = self.agent.get(self.url)
        title = page.title()

        self.assertEquals(title, "Google")

    def test_status_code(self):
        page = self.agent.get(self.url)
        code = page.status_code()

        self.assertEquals(code, 200)

    def test_html(self):
        page = self.agent.get(self.url)
        html = page.html()

        self.assertIsNotNone(html)

    def test_select(self):
        page   = self.agent.get(self.url)
        select = page.select("input[type=hidden]")[0]

        self.assertIsInstance(select, Tag)

    def test_form(self):
        page = self.agent.get(self.url)
        form = page.form("form[name=f]")

        self.assertIsInstance(form, Form)

    def test_submit(self):
        page   = self.agent.get(self.url)
        form   = page.form("form[name=f]")
        submit = form.submit()

        self.assertIsInstance(submit, Response)

    def test_links(self):
        page  = self.agent.get(self.url)
        links = page.links()
        link  = links[0]

        self.assertIsInstance(links, list)
        self.assertIsInstance(link, Link)

    def test_find_link(self):
        page = self.agent.get(self.url)

        name = page.find_link(name="YouTube")
        link = page.find_link(link="http://www.youtube.com/?gl=HK&tab=w1")

        name_regex = page.find_link(name_regex="Yo.*be")
        link_regex = page.find_link(link_regex=".*www.youtube.com.*")

        self.assertIsInstance(name, Link)
        self.assertIsInstance(link, Link)

        self.assertIsInstance(name_regex, Link)
        self.assertIsInstance(link_regex, Link)
