#!/usr/bin/env python

from distutils.core import setup, Command
import os
import os.path

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='toproxy',
    version='3.0',
    description='Simple Tornado Async HTTP Proxy',
    long_description=open('README.md').read(),
    keywords = ["tornado proxy","fengyun"],
    url='http://xiaorui.cc',
    author='ruifengyun',
    author_email='rfyiamcool@163.com',
    install_requires=['tornado'],
    packages=['toproxy'],
    license = "MIT",
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Topic :: Software Development :: Libraries :: Python Modules',
            ]
)
