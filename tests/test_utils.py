# -*- coding: utf-8 -*-

from .base_suite import BaseSuite
from motorise.utils import normalize_url

class TestUtils(BaseSuite):
    def test_normalize_url(self):
        case1  = normalize_url("http://hk.yahoo.com/a/b.html", "/")
        case2  = normalize_url("http://hk.yahoo.com/a/b.html", "../")
        case3  = normalize_url("http://hk.yahoo.com/a/b.html", "./a")
        case4  = normalize_url("http://hk.yahoo.com/a/b.html", "./abc/a.html")
        case5  = normalize_url("http://hk.yahoo.com/a/b.html", "../abc/a.html")
        case6  = normalize_url("http://hk.yahoo.com/a/b.html", "http://hk.yahoo.com/")
        case7  = normalize_url("http://hk.yahoo.com/a/b.html", "http://hk.yahoo.com/test")
        case8  = normalize_url("http://hk.yahoo.com/a/b.html", "/hk.yahoo.com/test")
        case9  = normalize_url("http://hk.yahoo.com/a/b.html", "/http://hk.yahoo.com/test")
        case10 = normalize_url("http://hk.yahoo.com/a/b.html", "?a=http://hk.yahoo.com/test")

        self.assertEqual(case1,  "http://hk.yahoo.com/")
        self.assertEqual(case2,  "http://hk.yahoo.com/")
        self.assertEqual(case3,  "http://hk.yahoo.com/a/a")
        self.assertEqual(case4,  "http://hk.yahoo.com/a/abc/a.html")
        self.assertEqual(case5,  "http://hk.yahoo.com/abc/a.html")
        self.assertEqual(case6,  "http://hk.yahoo.com/")
        self.assertEqual(case7,  "http://hk.yahoo.com/test")
        self.assertEqual(case8,  "http://hk.yahoo.com/hk.yahoo.com/test")
        self.assertEqual(case9,  "http://hk.yahoo.com/http:/hk.yahoo.com/test")
        self.assertEqual(case10, "http://hk.yahoo.com/a/b.html?a=http://hk.yahoo.com/test")
