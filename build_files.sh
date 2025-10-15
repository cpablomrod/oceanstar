#!/bin/bash
set -e

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Django version:"
python -m django --version

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Checking staticfiles_build folder..."
if [ -d "staticfiles_build" ]; then
  echo "✅ Folder exists!"
  ls -la staticfiles_build
else
  echo "❌ Folder not found!"
  exit 1
fi