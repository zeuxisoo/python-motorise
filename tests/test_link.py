# -*- coding: utf-8 -*-

from .base_suite import BaseSuite

class TestLink(BaseSuite):
    def test_text(self):
        page = self.agent.get(self.url_duckduckgo)
        link = page.find_link(name="About DuckDuckGo Duck it!")

        self.assertEqual(link.text(), "About DuckDuckGo Duck it!")

    def test_href(self):
        page = self.agent.get(self.url_duckduckgo)
        link = page.find_link(link="/about")

        self.assertEqual(link.href(), "/about")

    def test_id(self):
        page = self.agent.get(self.url_duckduckgo)
        link = page.find_link(name="Learn More")

        self.assertEqual(link.id(), "")
