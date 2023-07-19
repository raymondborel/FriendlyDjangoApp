#!/usr/bin/env bash

# set -o errexit  # exit on error

# pip install -r requirements.txt

# python manage.py collectstatic --no-input
# python manage.py migrate


# video method 
# Install Dependencies
pip3 install -r deps.txt

# Run Migration
python3 manage.py migrate