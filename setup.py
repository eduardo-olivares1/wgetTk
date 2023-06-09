#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="app",
    version="0.0",
    description="App description",
    author="Eduardo Olivares",
    packages=find_packages(exclude=["tests", "testing*"]),
    install_requires=["requests"],
    entry_points={"console_scripts": ["app = app.__main__:main"]},
)
