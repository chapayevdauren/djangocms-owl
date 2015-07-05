#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import djangocms_owl

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = djangocms_owl.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.md').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='djangocms-owl',
    version=version,
    description="""Djangocms plugin for owl carousel v1""",
    long_description=readme + '\n\n' + history,
    author='Lee Solway',
    author_email='lee@digitalanvil.co.uk',
    url='https://github.com/leesolway/djangocms-owl',
    packages=[
        'djangocms_owl',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='djangocms-owl',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
