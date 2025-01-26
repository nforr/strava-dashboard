#!/bin/bash

# Save the installed dependencies to requirements.txt
echo "Saving dependencies to requirements.txt..."
pip freeze > requirements.txt

# Deactivate the virtual environment
echo "Deactivating the virtual environment..."
deactivate

echo "Dependencies saved and virtual environment deactivated."

# Check if the virtual environment is not active
echo "Activated Python: $(which python)"