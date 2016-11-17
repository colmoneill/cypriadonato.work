#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Cypria Donato'
SITENAME = u'Cypria Donato'
SITESUBTITLE = u'Animation Artist'
SITEURL = 'http://cypriadonato.work'
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TYPOGRIFY = False


# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10


THEME = "output/theme/cypria-donato"
#THEME = "/usr/local/lib/python2.7/dist-packages/pelican/themes/notmyidea"
#THEME = "/usr/local/lib/python2.7/dist-packages/pelican/themes/simple"
CSS_FILE = 'screen.css'
USE_FOLDER_AS_CATEGORY = True
ARTICLE_PATHS = ['Blog/', 'Projets/', 'Contact/',]
INDEX_SAVE_AS = 'all_index.html'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (('Projets', 'projets.html'),
             ('Contact', 'contact.html'),
             ('Blog', 'blog.html'),
             ('Book', 'book.html'),)


##--------------------
### URL SETTINGS ###

CATEGORY_URL = '{slug}.html'
CATEGORY_SAVE_AS = '{slug}.html'

##--------------------
### PLUGINS ###

PLUGIN_PATHS = ["plugins"]
PLUGINS = ['representative_image', 'collate_content']
