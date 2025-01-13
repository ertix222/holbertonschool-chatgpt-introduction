#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    ----------------------
    This function calculates the factorial of a given non-negative integer `n` 
    using recursion. The factorial of a number is the product of all positive integers 
    less than or equal to the number. For `n = 0`, the factorial is defined as `1`.

    Parameters:
    -----------
    n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
    --------
    int: The factorial of the input number `n`.
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n-1)  # Recursive case

# Read input from the command line, compute the factorial, and print the result
try:
    f = factorial(int(sys.argv[1]))
    print(f)
except (IndexError, ValueError):
    print("Usage: python3 script_name.py <non-negative integer>")
