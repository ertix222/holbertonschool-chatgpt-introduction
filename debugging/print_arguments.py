#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("Aucun argument fourni.")
else:
    print("Liste des arguments :")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")
