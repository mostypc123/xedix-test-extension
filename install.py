#!/usr/bin/env python
import os
import re

# ALWAYS ask for path - no automatic detection
file_path = input("Enter full path to extension file: ")

# Verify path exists
while not os.path.exists(file_path):
    print(f"Error: Path '{file_path}' does not exist")
    file_path = input("Enter full path to extension file: ")

# Read and modify the file
with open(file_path, "r") as f:
    content = f.read()

modified = re.sub(
    r'def main\(\):(.*?)(return|$)',
    r'def main():\1    print("hello world")\n\2',
    content,
    flags=re.DOTALL
)

with open(file_path, "w") as f:
    f.write(modified)

print(f"Successfully modified {file_path}")
