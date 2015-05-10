# coding: utf-8
from distutils.core import setup

setup(
    name='sw-django-utils',
    version='0.0.6',
    description='Soft Way company django utils.',
    author='Telminov Sergey',
    url='https://github.com/telminov/sw-django-utils',
    packages=['djutils', 'djutils.views', 'djutils.tests'],
    license='The MIT License',
    install_requires=[
        'django',
    ],
)
