# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='frappe_traceback_collector',
    version=version,
    description='A Collector and Formatter for Tracebacks in Frappe',
    author='Maxwell Morais',
    author_email='max.morais.dmm@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
