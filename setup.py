#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [requirement for requirement in open('requirements.txt')]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Raja CSP Raman",
    author_email="raja@tactii.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
    ],
    description="Pretty Metrics help build a lot of basic models without much code and helps understand which models works better without any parameter tuning",
    entry_points={"console_scripts": ["prettymetrics=prettymetrics.cli:main",],},
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="prettymetrics",
    name="prettymetrics",
    packages=find_packages(include=["prettymetrics", "prettymetrics.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/tactlabs/prettymetrics",
    version='0.0.1',
    zip_safe=False,
)
