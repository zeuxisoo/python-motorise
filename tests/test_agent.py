# -*- coding: utf-8 -*-

from .base_suite import BaseSuite
from motorise import Page
from requests.models import Response

class TestAgent(BaseSuite):
    def test_get(self):
        page = self.agent.get(self.url)

        self.assertIsInstance(page, Page)

    def test_submit(self):
        page = self.agent.get(self.url)

        form   = page.form("form[name=f]")
        form.set_field("q", "github")
        submit = self.agent.submit(form)

        self.assertIsInstance(submit, Response)
