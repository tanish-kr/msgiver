# -*- coding: utf-8 -*-

from pip.req import parse_requirements
from setuptools import setup


setup(
        name="msgiver",
        version="0.0.1",
        packages=parse_requirements('requirements.txt'),
        url="",
        license="",
        author="Tatsunori Nishikori",
        author_email="tora.1986.tatsu@gmail.com",
        package_data={},
        description="msgiver will deliver the text to Messenger"
)
