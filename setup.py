#!/usr/bin/env python

from distutils.core import setup, Command
import os
import os.path

setup(
    name='toproxy',
    version='2.0',
    description='Simple Tornado Async HTTP Proxy',
    url='http://xiaorui.cc',
    author='ruifengyun',
    author_email='rfyiamcool@163.com',
    long_description=open('README.md').read(),
    install_requires=['tornado'],
    packages=['toproxy'],
)
