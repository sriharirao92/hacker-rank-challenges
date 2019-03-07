#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    indices = [i for i, e in enumerate(c) if e == 0]
    tracker=0
    jump=0
    while(tracker<max(indices)):
        if(tracker+2 in indices):
            tracker+=2
            jump+=1
        else:
            tracker+=1
            jump+=1
    return(jump)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
