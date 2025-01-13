#!/usr/bin/python3
import sys

# Check if arguments are provided
if len(sys.argv) == 1:
    print("No arguments provided. Please pass some arguments when running the script.")
else:
    print("Arguments passed to the script:")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")
