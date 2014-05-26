import sys
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import rdio_export

requires = [
    'Rdio',
    'wsgiref',
]

requires_links = [
    'https://github.com/rdio/rdio-python/archive/master.zip#egg=rdio-python-0.2',
]

setup(
    name='python-rdio-export',
    version=rdio_export.__version__,
    description='A command-line utility for exporting an Rdio collection.',
    long_description=open('README.rst').read(),
    license=open('LICENSE').read(),
    author='Tristan Waddington',
    author_email='tristan.waddington@gmail.com',
    url='https://github.com/twaddington/python-rdio-export',
    install_requires=requires,
    dependency_links=requires_links,
    packages=['rdio_export'],
    scripts=['bin/rdio-export'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
