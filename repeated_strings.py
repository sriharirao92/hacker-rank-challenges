#!/bin/python

import math
import os
import random
import re
import sys
from collections import Counter
import math

# Complete the repeatedString function below.
def repeatedString(s, n):
    if(n >= 1000000000000):
        return n
    else:
        mult = n/len(s)+1
        redundant = len(s)*mult-n
        lastChars = Counter(list(s[-redundant:]))["a"]
        return Counter(list(s))["a"]*(mult)-lastChars

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
