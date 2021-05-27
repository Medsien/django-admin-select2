#!/usr/bin/env python

from distutils.core import setup
import os


try:
    from pypandoc import convert_file

    def get_long_description():
        return convert_file('README.md', 'rst')
except Exception:
    def get_long_description():
        pass


def get_package_data(package):
    start = len(package) + 1  # strip package name
    for path, dirs, files in os.walk(package):
        for file in files:
            if file.startswith('.') or file.endswith('.py') or file.endswith('.pyc'):
                continue
            yield os.path.join(path[start:], file)


setup(
    name='django3_admin_select2',
    version='0.1.0',
    description='Enable select2 for Django3 admin select inputs',
    long_description=get_long_description(),
    author='Medsien, Inc.',
    author_email='hello@medsien.com',
    url='https://github.com/Medsien/django3-admin-select2',
    packages=[
        'django3_admin_select2',
    ],
    package_data={
        'django3_admin_select2': list(get_package_data('django3_admin_select2')),
    },
    keywords=['django', 'django-admin', 'select2'],
)
