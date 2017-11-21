#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Careotica'
SITENAME = "Careotica"
SITEURL = ''
#SITEURL = 'http://careoti.ca'

PATH = 'content'

TIMEZONE = 'America/Halifax'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



# Blogroll
LINKS = (('Home', '/'),
         ('Makeup Gallery', 'https://www.instagram.com/beautybycareotica/'),
         ('Bandcamp', 'https://careotica.bandcamp.com/'),
         ('Soundcloud', 'https://soundcloud.com/careoticalovicious-1'),
         ('Instagram', 'https://www.instagram.com/beautybycareotica/'),
         ('Twitter', 'https://twitter.com/careoticalov?lang=en'),
         ('eMail', 'mailto:careotica@gmail.com'),
        )

DEFAULT_PAGINATION = 20
THEME = './pelican-themes/Flex'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
