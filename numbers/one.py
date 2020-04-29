"""
Find PI to the Nth Digit -
Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.
"""

import math
import sys

try:
    decimal_places = input("Enter the number of decimal places: ")
    if int(decimal_places) <= 30:
        print(format(math.pi, '.{}f'.format(decimal_places)))
    else:
        print("Enter a value between 0 and 30")
        sys.exit(1)
except ValueError as e:
    print("Enter a valid integer value")
    sys.exit(1)