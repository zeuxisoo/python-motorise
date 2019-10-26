# -*- coding: utf-8 -*-

from .base_suite import BaseSuite
from motorise import Page, Form, Link
from bs4.element import Tag

class TestPage(BaseSuite):
    def test_title(self):
        page  = self.agent.get(self.url_google)
        title = page.title()

        self.assertEqual(title, "Google")

    def test_status_code(self):
        page = self.agent.get(self.url_google)
        code = page.status_code()

        self.assertEqual(code, 200)

    def test_html(self):
        page = self.agent.get(self.url_google)
        html = page.html()

        self.assertIsNotNone(html)

    def test_select(self):
        page   = self.agent.get(self.url_google)
        select = page.select("input[type=hidden]")[0]

        self.assertIsInstance(select, Tag)

    def test_form(self):
        page  = self.agent.get(self.url_google)
        form1 = page.form("form[name=f]")
        form2 = page.form("form", index=0)

        self.assertIsInstance(form1, Form)
        self.assertIsInstance(form2, Form)

    def test_submit(self):
        page   = self.agent.get(self.url_google)
        form   = page.form("form[name=f]")
        submit = form.submit()

        self.assertIsInstance(submit, Page)

    def test_links(self):
        page  = self.agent.get(self.url_google)
        links = page.links()
        link  = links[0]

        self.assertIsInstance(links, list)
        self.assertIsInstance(link, Link)

    def test_find_link(self):
        page = self.agent.get(self.url_duckduckgo)

        name = page.find_link(name="About DuckDuckGo Duck it!")
        link = page.find_link(link="/about")

        name_regex = page.find_link(name_regex=r'About\sDuckDuckGo\sDuck\sit!')
        link_regex = page.find_link(link_regex=r'/(about)')

        self.assertIsInstance(name, Link)
        self.assertIsInstance(link, Link)

        self.assertIsInstance(name_regex, Link)
        self.assertIsInstance(link_regex, Link)

    def test_is_include(self):
        page = self.agent.get(self.url_google)

        self.assertTrue(page.is_include("YouTube"))
        self.assertTrue(page.is_include(u"地圖"))
