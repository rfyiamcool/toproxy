#!/usr/bin/env python

from distutils.core import setup, Command
import os
import os.path

setup(
    name='toproxy',
    version='0.8',
    description='tornado asynchronous HTTP proxy',
    url='http://xiaorui.cc',
    author='ruifengyun',
    author_email='rfyiamcool@163.com',
    long_description=open('README.md').read(),
    install_requires=['tornado'],
    packages=['toproxy'],
)
