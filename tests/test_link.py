# -*- coding: utf-8 -*-

from .base_suite import BaseSuite

class TestLink(BaseSuite):
    def test_text(self):
        page = self.agent.get(self.url)
        link = page.find_link(name="YouTube")

        self.assertEquals(link.text(), "YouTube")

    def test_href(self):
        page = self.agent.get(self.url)
        link = page.find_link(link="http://www.youtube.com/?gl=HK&tab=w1")

        self.assertEquals(link.href(), "http://www.youtube.com/?gl=HK&tab=w1")

    def test_id(self):
        page = self.agent.get(self.url)
        link = page.find_link(name="YouTube")

        self.assertEquals(link.id(), "")
