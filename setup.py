# -*- coding: utf-8 -*-

# Author Tatsunori Nishikori <tora.1986.tatsu@gmail.com>
# Public License, available in the accompanying LICENSE.txt file.


"""
setup script for msgiver
"""

from pip.req import parse_requirements
import sys
import os

sys.path.insert(0, os.path.abspath("msgiver"))
import msgiver

try:
    from setuptools import setup, find_packages
except ImportError:
    print("msgiver now needs setuptools in order to build. Install it using"
            " your package manager (usually python-setuptools) or via pip (pip"
            " install setuptools).")
    sys.exit(1)

with open("requirements.txt") as requiremens_file:
    try:
        install_requirements = requiremens_file.read().splitlines()
    except Exception as e:
        print(e.message)
        print("Unable to read requirements from the requirements.txt file")
        sys.ext(2)

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("requirements/dev.txt") as test_requirements_file:
    try:
        test_install_requirements = test_requirements_file.read().splitlines()
    except Exception as e:
        print(e.message)
        print("Unable to read requirements from the requirements/dev.txt file")
        sys.ext(3)

setup(
        name="msgiver",
        version="0.1.0",
        url="https://github.com/kitaro-tn/msgiver",
        license="MIT",
        test_suite="msgiver",
        author="Tatsunori Nishikori",
        author_email="tora.1986.tatsu@gmail.com",
        description="msgiver will deliver the text to Messenger",
        long_description=readme,
        install_requires=install_requirements,
        tests_require=test_install_requirements,
        packages=find_packages(exclude=("tests", "tests.*")),
        classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: MIT License',
        ],
        # package_data={},
)
