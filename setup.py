#!/usr/bin/env python
# coding: utf8

import os
import setuptools
import sys


#: The name of the package on PyPi
PYPI_PACKAGE_NAME = 'pynput'

#: The name of the main Python package
MAIN_PACKAGE_NAME = 'pynput'

#: The package URL
PACKAGE_URL = 'https://github.com/moses-palmer/pynput'

#: The author email
AUTHOR_EMAIL = 'moses.palmer@gmail.com'

#: The runtime requirements
RUNTIME_PACKAGES = []

if sys.version_info.major < 3:
    RUNTIME_PACKAGES.append('enum34')

#: Additional requirements used during setup
SETUP_PACKAGES = RUNTIME_PACKAGES + [
    'sphinx >=1.3.1']


# Read globals from ._info without loading it
INFO = {}
with open(os.path.join(
        os.path.dirname(__file__),
        'lib',
        MAIN_PACKAGE_NAME,
        '_info.py')) as f:
    for line in f:
        try:
            name, value = (i.strip() for i in line.split('='))
            if name.startswith('__') and name.endswith('__'):
                INFO[name[2:-2]] = eval(value)
        except ValueError:
            pass


# Load the read me
try:
    with open(os.path.join(
            os.path.dirname(__file__),
            'README.rst')) as f:
        README = f.read()

    with open(os.path.join(
            os.path.dirname(__file__),
            'mouse-usage.rst')) as f:
        README += '\n\n' + f.read()
except IOError:
    README = ''


# Load the release notes
try:
    with open(os.path.join(
            os.path.dirname(__file__),
            'CHANGES.rst')) as f:
        CHANGES = f.read()
except IOError:
    CHANGES = ''


setuptools.setup(
    name=PYPI_PACKAGE_NAME,
    version='.'.join(str(i) for i in INFO['version']),
    description='Monitor and control user input devices',
    long_description=README + '\n\n' + CHANGES,

    install_requires=RUNTIME_PACKAGES,
    setup_requires=RUNTIME_PACKAGES + SETUP_PACKAGES,

    author=INFO['author'],
    author_email=AUTHOR_EMAIL,

    url=PACKAGE_URL,

    packages=setuptools.find_packages(
        os.path.join(
            os.path.dirname(__file__),
            'lib')),
    package_dir={'': 'lib'},
    zip_safe=True,

    test_suite='tests',

    license='GPLv3',
    keywords='control mouse, mouse input',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows NT/2000',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Monitoring'])
