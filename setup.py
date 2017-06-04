from distutils.core import setup
from setuptools import setup, find_packages

setup(name='TEviST',
      version='0.1',
      description='A toolkit to visualize test results',
      author='Simone Robutti',
      author_email='simone.robutti@gmail.com',
      packages=find_packages(where="."),
      )
