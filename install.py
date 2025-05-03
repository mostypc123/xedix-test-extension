#!/usr/bin/env python
import os
import re

# Try to find extension file or ask for path
file_path = "extension_mainfn.py" if os.path.exists("extension_mainfn.py") else input("Path: ")

# Read the file content
with open(file_path, "r") as f:
    content = f.read()

# Insert print statement into main() function
modified = re.sub(r'def main\(\):(.*?)(return|$)', r'def main():\1    print("hello world")\n\2', content, flags=re.DOTALL)

# Write back to file
with open(file_path, "w") as f:
    f.write(modified)
