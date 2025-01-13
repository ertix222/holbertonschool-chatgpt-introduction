#!/usr/bin/python3
import sys

# Check if any arguments are provided
if len(sys.argv) == 1:
    print("No arguments provided.")
else:
    print("Arguments passed to the script:")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")
