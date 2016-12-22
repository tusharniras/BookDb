# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='BookDb',
    version='0.0.1',
    description='Books database RESTful API',
    long_description=readme,
    author='Tushar Niras',
    author_email='tnniras@gmail.com',
    url='https://github.com/tusharniras/BookDb.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)