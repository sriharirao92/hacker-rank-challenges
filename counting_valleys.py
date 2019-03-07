#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count = 0
    neg = 0
    valleys = 0
    for each in s:
        if(each == "D"):
            count-=1
        elif(each == "U"):
            count+=1
        if(count < 0):
            neg=-1
        elif(count > 0):
            neg=1
        elif(count == 0 and neg==-1):
            valleys+=1
            neg=0
    return(valleys)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
