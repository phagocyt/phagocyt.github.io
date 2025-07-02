#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Hui Ji'
SITENAME = 'My Site'
SITEURL = ''

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}


PATH = 'content'

TIMEZONE = 'America/Los_Angeles'  # change for your timezone
DEFAULT_LANG = 'en'

# Theme (optional)
THEME = 'themes/pelican-fh5co-marble'

# Make sure your pages show in the menu:
DISPLAY_PAGES_ON_MENU = True

MENUITEMS = [
    ('Home', '/'),
    # ('Blog', '/archives.html'),
    ('Side Projects', '/side-projects.html'),
]



# Paths
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']



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

