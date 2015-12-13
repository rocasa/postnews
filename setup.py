#!/usr/bin/env python
# coding: utf-8

from distutils.core import setup

setup(name='postnews',
      version='0.6',
      description='Post Usenet articles via NNTP from the command line',
      long_description="""Postnews is used to post Usenet articles (including headers) from
stdin or a file to a nntp server. The article must at least contain the
headers 'From:','Newsgroups:', 'Subject:', a newline and a body.""",
      author=['Michael Waschbüsch','Robert James Clay'],
      author_email=['waschbuesch@users.sourceforge.net','jame@rocasa.us'],
      license='GPLv2+',
      platforms='any',
      url='http://sourceforge.net/projects/postnews/',
      scripts=['postnews.py'],
     )
