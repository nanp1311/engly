#!/usr/bin/python3
from setuptools import setup, find_packages

setup(
<<<<<<< HEAD
    name="enly",
=======
    name="anly",
>>>>>>> 21bf9f98d222dc8f405582fdc7af8a54275bcc1f
    version='1.0',
    description='English Learning Application',
    author='nanp1311',
    author_email='pengin.na11@gmail.com',
    url='https://github.com/nanp1311/Enly',
     packages=find_packages(),
    entry_points="""
      [console_scripts]
<<<<<<< HEAD
      enly = enly.title:main
=======
      anly = anly.title:main
>>>>>>> 21bf9f98d222dc8f405582fdc7af8a54275bcc1f
    """,
)