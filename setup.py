#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="wgettk",
    version="0.0",
    description="App description",
    author="Eduardo Olivares",
    packages=find_packages(exclude=["tests", "testing*"]),
    install_requires=["requests"],
    entry_points={"console_scripts": ["wgettk = wgettk.__main__:main"]},
)
