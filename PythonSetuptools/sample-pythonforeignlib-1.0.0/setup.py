#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, Extension, setup
from os.path import join, dirname

setup(
    name='sample-pythonforeignlib',
    version="1.0.0",
    description="Biblioteca instalável exemplo comm funções estrangeiras",
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
    scripts=[
        'samplepythonprogram.py',
        ],
    ext_modules=[
        Extension(
            name="my_functions.so",
            sources=["my_functions.c"],
            ),
        ]
    )
