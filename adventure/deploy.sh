#!/bin/bash

# Remove previous distributions
rm -rf dist/

# Create a source distribution
python setup.py sdist

# Create a wheel distribution
python setup.py bdist_wheel

# Upload to TestPyPI using twine
twine upload --repository-url https://pypi.org/legacy/ dist/*

# Prompt the user to confirm if they want to upload to actual PyPI
read -p "Upload to PyPI? (y/n) " -n 1 -r
echo    # move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    twine upload dist/*
fi
