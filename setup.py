from setuptools import setup

setup(
  name = 'pdftablr',
  packages = ['pdftablr'],
  scripts = ['pdftable'],
  version = '0.1.0',
  description = "Python3 implementation of Kyle Cronan's pdftable module, with unit tests",
  license = 'GPL',
  author = 'Phil Gooch and Kyle Cronan',
  author_email = 'philgooch@users.noreply.github.com',
  url = 'https://github.com/philgooch/pdftable',
  download_url = 'https://github.com/philgooch/pdftable/archive/v0.1.0.tar.gz',
  keywords = ['python3', 'pdf', 'table-extraction', 'tables', 'information-extraction'],
  classifiers = [],
  zip_safe=False,
)
