# -*- coding: utf-8 -*-

from .base_suite import BaseSuite
from motorise import Page

class TestAgent(BaseSuite):
    def test_get(self):
        page = self.agent.get(self.url_google)

        self.assertIsInstance(page, Page)

    def test_submit(self):
        page = self.agent.get(self.url_google)

        form   = page.form("form[name=f]")
        form.set_field("q", "github")
        submit = self.agent.submit(form)

        self.assertIsInstance(submit, Page)

    def test_get_kwargs(self):
        page = self.agent.get(self.url_verify_false, verify=False)

        self.assertIsInstance(page, Page)
