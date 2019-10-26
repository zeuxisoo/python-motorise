# -*- coding: utf-8 -*-

from urllib.parse import urlparse, urljoin, urlunparse
import posixpath

def normalize_url(base, url):
    join = urljoin(base, url)
    url  = urlparse(join)
    path = posixpath.normpath(url[2])

    return urlunparse(
        (url.scheme, url.netloc, path, url.params, url.query, url.fragment)
    )
