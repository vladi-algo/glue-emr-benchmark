#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
    name='kds-siege',
    version='0.0.1',
    description='Kinesis Data Streams load tester and benchmarking utility',
    long_description=open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md')
    ).read(),
    long_description_content_type='text/markdown',
    author='Dor Fibert, Vladislav Feigin',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['setuptools', 'click'],
    entry_points={'console_scripts': ['kds-siege=kds_siege.main:main']},
)