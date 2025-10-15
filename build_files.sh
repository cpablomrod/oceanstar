#!/bin/bash
set -e

echo "=== Starting build_files.sh ==="

# Install pip if missing
echo "Checking pip..."
python -m ensurepip --upgrade || curl https://bootstrap.pypa.io/get-pip.py | python

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Verify Django
echo "Django version:"
python -m django --version

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Verify staticfiles_build folder
if [ -d "staticfiles_build" ]; then
  echo "✅ Folder exists!"
  ls -la staticfiles_build
else
  echo "❌ Folder not found!"
  exit 1
fi

echo "=== Finished build_files.sh ==="