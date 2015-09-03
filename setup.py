#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='gevent_openssl',
    version='1.2',
    description='A gevent wrapper for pyOpenSSL',
    author='Travis Brown',
    author_email='travis@bryx.com',
    url='https://github.com/bryx-inc/gevent_openssl',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    license='New BSD',
    platforms='any',
    install_requires=['pyOpenSSL>=0.11', 'gevent'],
)
