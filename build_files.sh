#!/bin/bash
set -e  # Stop on any error

echo "=== Starting build_files.sh ==="

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Run collectstatic
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Check if the folder exists
if [ -d "staticfiles_build" ]; then
  echo "✅ staticfiles_build folder created successfully!"
  ls -la staticfiles_build
else
  echo "❌ ERROR: staticfiles_build folder not found!"
  exit 1
fi

echo "=== Finished build_files.sh ==="