# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setuptools import find_packages


setup(
    name='demo-jino-prueba-up',
    version=__import__('access_reset_demo').__version__,
    author='Jino Huayas',
    author_email='jinohuayas@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/jinohuayas/demo-jino-prueba-up.git',
    license='BSD licence, see LICENSE file',
    description='Class-based views for access reset demo.',
    long_description=open('README.rst').read(),
    install_requires=[
        'Django>=1.8',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    test_suite='',
    zip_safe=False,
)
