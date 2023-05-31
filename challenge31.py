#!/usr/bin/python3

# Challenge 31
# Dylan Dempsey
# 5/30/23
# Create a python script  that will:

# Prompt the user to type in a file name to search for.
# Prompt the user for a directory to search in.
# Search each file in the directory by name.

# For each positive detection, print to the screen the file name and location.
# At the end of the search process, print to the screen how many files were searched and how many hits were found.
# The script must successfully execute on both Ubuntu Linux 20.04 Focal Fossa and Windows 10.

# Main

import os

# Prompt the user for a file name and a directory
file_name = input("Enter the file name to search for: ")
dir_name = input("Enter the directory to search in: ")

# Initialize count variables
total_files = 0
total_hits = 0

# Walk through the directory
for root, dirs, files in os.walk(dir_name):
    total_files += len(files)
    for file in files:
        if file == file_name:
            total_hits += 1
            print(f"Found: {os.path.join(root, file)}")

# Print totals
print(f"Searched {total_files} files.")
print(f"Found {total_hits} instances of {file_name}.")

# End

# ChatGPT was referenced for this code.
