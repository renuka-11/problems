#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split(' ')
    result=''
    for word in words:
        if word:
            first_letter = word[0].upper()
            remaining_letter = word[1:]
            result+=first_letter+remaining_letter+' '
        else:
            result+=' '
    return result
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
