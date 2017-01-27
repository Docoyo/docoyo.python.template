'''
  Some description of the wonderful module
'''
import os
from setuptools import setup


def read(fname):
  '''
    Utility function to read the README file.
  '''
  return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="my_package",
    version="0.0.1",
    author="Nicolaj Kirchhof",
    author_email="nico@docoyo.com",
    description=("A wonderful module."),
    license="BSD",
    keywords="some keywords",
    url="http://docoyo.com",
    package_dir={
        'my_package': 'my_package',
        'my_package.my_subpackage': 'my_package/my_subpackage'
    },
    packages=['my_package', 'my_package.my_subpackage', 'test'],
    long_description=read('../README.md'),
    include_package_data=True,
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],)
