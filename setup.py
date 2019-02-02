import sys

from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='virgencita',
    version='1.0',
    description='Little virgin',
    packages=['virgencita'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==1.0.2',
        'forecastiopy==0.22',
        'geoip2==2.9.0',
    ],
    extras_require={
        'lint': ['pycodestyle'],
        'test': ['tox'],
    },
)
