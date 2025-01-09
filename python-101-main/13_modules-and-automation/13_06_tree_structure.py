# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.
from pathlib import Path

current_directory = Path("/Users/seburke/PyPlayground/codingnomads/python-101-main")

for python_file in current_directory.rglob("*.py"):
    relative_path = python_file.relative_to(current_directory)
    print(f"{relative_path}")