#!/bin/bash

# Activate the virtual environment
source stravavenv/bin/activate

# Check if the virtual environment is active
echo "Activated Python: $(which python)"

# Install requirements if a requirements.txt file exists
if [ -f "requirements.txt" ]; then
  echo "Installing dependencies from requirements.txt..."
  pip install -r requirements.txt
else
  echo "No requirements.txt file found. Skipping installation."
fi

echo "Virtual environment activated and dependencies installed."