#!/usr/bin/env python
# The script above should be executable but isn't - will trigger check-shebang-scripts-are-executable

from setuptools import setup, find_packages

# Misspelled word - will trigger codespell
setup(
    name="sample_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyyaml",
    ],
    author="Antonio Pérez",
    author_email="antperez@apexsystems.com",
    description="A sample project for demonstarting pre-commit hooks",
    keywords="sample, pre-commit",
    python_requires=">=3.12",
)