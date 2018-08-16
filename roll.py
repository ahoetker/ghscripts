#!/usr/bin/env python3

import sys
from random import randint

number_of_args = len(sys.argv)  # including name of file

if number_of_args == 1:
    roll = randint(0, 100)
elif number_of_args == 2:
    try:
        max = int(sys.argv[1])
    except ValueError:
        raise AssertionError("Arguments must be integers.")
    roll = randint(0, max)
elif number_of_args == 3:
    try:
        min = int(sys.argv[1])
        max = int(sys.argv[2])
    except ValueError:
        raise AssertionError("Arguments must be integers.")
    roll = randint(min, max)
else:
    roll = None
    print("Incorrect number of arguments")

if roll is not None:
    print(roll)
