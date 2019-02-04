import sys

from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='virgencita',
    version='1.0',
    description='Little virgin',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    #packages=['virgencita'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==1.0.2',
        'forecastiopy==0.22',
        'geoip2==2.9.0',
        'requests==2.20.0',
        'requests-cache==0.4.13',
    ],
    extras_require={
        'lint': ['pycodestyle'],
        'test': ['tox'],
    },
)
