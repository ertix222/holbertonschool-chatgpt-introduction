#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement `n` to prevent infinite loop
    return result

# Ensure a command-line argument is provided
if len(sys.argv) < 2:
    print("Usage: python3 script_name.py <non-negative integer>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
    f = factorial(num)
    print(f"The factorial of {num} is: {f}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
