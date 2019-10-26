# -*- coding: utf-8 -*-

import unittest
from motorise import Agent

class BaseSuite(unittest.TestCase):
    def setUp(self):
        self.agent            = Agent()
        self.url_google       = "https://www.google.com.hk/"
        self.url_duckduckgo   = "https://duckduckgo.com/"
        self.url_verify_false = "https://stackoverflow.com/"
