#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
from os.path import join, dirname

setup(
    name='sample-venvpythonlib',
    version="1.0.0",
    description="Biblioteca instalável exemplo",
    author="SIDIL",
    author_email="sidil@uniaolisboa-cgtp.pt",
    classifiers=[
        "Topic :: Software Development :: Libraries",
        ],
    install_requires=[],
    python_requires='>=3.10',
    extras_require={},
    tests_require=[],
    packages=[
        'samplepythonlibmodules',
        ],
    )
