#!/usr/bin/python
from setuptools import setup, find_packages


setup(
    name='bugimporters',
    version=0.1,
    author='Various contributers to the OpenHatch project, Berry Phillips',
    author_email='all@openhatch.org, berryphillips@gmail.com',
    packages=find_packages(),
    description='Bug importers for the OpenHatch project',
    install_requires=[
        'atom',
        'gdata',
        'lxml',
        'pyopenssl',
        'unicodecsv',
    ],
)
