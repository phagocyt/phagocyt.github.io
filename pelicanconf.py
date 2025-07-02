#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Hui Ji'
SITENAME = 'My Website'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'  # change for your timezone
DEFAULT_LANG = 'en'

# Paths
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']

# Theme (optional)
THEME = 'theme'

# URLs
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

# Feed generation (disable while developing)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

RELATIVE_URLS = True
