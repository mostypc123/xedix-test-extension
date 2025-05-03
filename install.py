import os
import re

file_path = input("Path: ").strip()

# Verify path exists
while not os.path.exists(file_path):
    print(f"Error: Path '{file_path}' not found")
    file_path = input("Path: ").strip()

# Read and modify the file
with open(file_path, "r+") as f:
    content = f.read()
    modified = re.sub(
        r'def main\(\):',
        'def main():\n    print("hello world")',
        content
    )
    f.seek(0)
    f.write(modified)
    f.truncate()

print(f"Modified {file_path}")
