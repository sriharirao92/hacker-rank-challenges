#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the matrixRotation function below.

def rotate(l, n):
    return l[-n:] + l[:-n]

def matrixRotation(matrix, r):
    mat = matrix
    matNew = copy.deepcopy(mat)

    m = len(mat)
    n = len(mat[0])

    layer1 = []
    minx=0
    miny=0
    maxx=m
    maxy=n

    for o in range(0,int(min(m,n)/2),1):
        for i in range(minx+1,maxx,1):
            layer1.append(mat[i][miny])
    
        for i in range(miny+1,maxy,1):
            layer1.append(mat[maxx-1][i])
    
        for i in range(maxx-2,minx-1,-1):
            layer1.append(mat[i][maxy-1])
    
        for i in range(maxy-2,miny-1,-1):
            layer1.append(mat[minx][i])

        if(r >= len(layer1)):
            rot = r % len(layer1)
        else:
            rot = r
    
        newLayer1 = rotate(layer1,rot)    

        for i in range(minx+1,maxx,1):
            matNew[i][miny] = newLayer1[i-(minx+1)]
        newLayer1 = newLayer1[maxx-(minx+1):]
        
        for i in range(miny+1,maxy,1):
            matNew[maxx-1][i] = newLayer1[i-(miny+1)]
        newLayer1 = newLayer1[maxy-(minx+1):] 
    
        for i in range(maxx-2,minx-1,-1):
            matNew[i][maxy-1] = newLayer1[abs(i-(maxx-2))]
        newLayer1 = newLayer1[maxx-(minx+1):]   
    
        for i in range(maxy-2,miny-1,-1):
            matNew[minx][i] = newLayer1[abs(i-(maxy-2))]

        maxx = maxx-1
        maxy = maxy-1
        minx = minx+1
        miny = miny+1

        layer1 = []
        newLayer1 = []
    
    for row in range(m):
        for col in range(n):
            print(matNew[row][col], end=" ")
        print()

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
