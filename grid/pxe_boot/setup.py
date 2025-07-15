#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2024 CNRS and University of Strasbourg
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from setuptools import setup

__author__ = 'Yannick Patois'
__email__ = 'yannick.patois@iphc.cnrs.fr'
__version__ = '0.1'

setup(
    name='pxe_boot',
    version=__version__,
    description='Creates files to be used for PXE booting from ansible data',
    long_description='''
        TBD.
    ''',
    classifiers=[
        'Development Status :: 1 - Production/Stable',
        'Environment :: Console',
        'Environment :: Other Environment',
        'Programming Language :: Python :: 3',
        ],
    keywords='',
    author=__author__,
    author_email=__email__,
    url='https://github.com/YPatois/update-vo-config/',
    license='Apache License, Version 2.0',
    python_requires='3.12',
    scripts=['pxe_boot'],
)
