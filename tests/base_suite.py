# -*- coding: utf-8 -*-

import unittest
from motorise import Agent

class BaseSuite(unittest.TestCase):
    def setUp(self):
        self.agent = Agent()
        self.url   = "http://www.google.com"
