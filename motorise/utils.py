# -*- coding: utf-8 -*-

import urlparse
import posixpath

def normalize_url(base, url):
    join = urlparse.urljoin(base, url)
    url  = urlparse.urlparse(join)
    path = posixpath.normpath(url[2])

    return urlparse.urlunparse(
        (url.scheme, url.netloc, path, url.params, url.query, url.fragment)
    )
