# -*- coding: utf-8 -*-

from .base_suite import BaseSuite
from motorise import Form
from requests.models import Response

class TestForm(BaseSuite):
    def test_load_hidden_fields(self):
        page = self.agent.get(self.url)

        form = page.form("form[name=f]")

        self.assertIsNotNone(form.fields)

    def test_set_field(self):
        page = self.agent.get(self.url)

        form = page.form("form[name=f]")
        form.set_field('q', 'github')

        self.assertIn('q', form.fields)
        self.assertEquals('github', form.fields['q'])

    def test_submit(self):
        page = self.agent.get(self.url)

        form   = page.form("form[name=f]")
        form.set_field('q', 'github')
        submit = form.submit()

        self.assertIsInstance(submit, Response)
