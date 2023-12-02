#!/usr/bin/python3
from setuptools import setup, find_packages

setup(
    name="anly",
    version='1.0',
    description='English Learning Application',
    author='nanp1311',
    author_email='pengin.na11@gmail.com',
    url='https://github.com/nanp1311/Anly',
     packages=find_packages(),
    entry_points="""
      [console_scripts]
      anly = anly.title:main
    """,
)