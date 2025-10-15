#!/bin/bash

# Build script for Vercel deployment
echo "Build started..."

# Install dependencies
python3.9 -m pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

echo "Build completed!"