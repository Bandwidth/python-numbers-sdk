import os
from setuptools import setup, find_packages

NAME = "bandwidth-numbers-sdk"
VERSION = os.environ['RELEASE_VERSION']

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    REQUIRES = f.read().splitlines()

PYTHON_REQUIRES = ">=3.7"

setup(
    name=NAME,
    version=VERSION,
    description="Bandwidth Numbers SDK",
    author="Bandwidth",
    author_email="letstalk@bandwidth.com",
    url="https://github.com/bandwidth/python-numbers-sdk",
    keywords=["Bandwidth", "Numbers"],
    python_requires=PYTHON_REQUIRES,
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown'
)
