#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxRegion' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def maxRegion(grid):
    # Write your code here
    maxR = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 1:
                maxR = max(maxR, 1+search(grid,y,x))
    return maxR
def search(grid, y,x):
    grid[y][x] = 2
    xway,yway = [-1,0,1],[-1,0,1]
    res = 0
    print(y,x)
    for dy in yway:
        for dx in xway:
            if  dy+y<0 or dx+x<0 or dy+y>=len(grid) or dx+x>=len(grid[0]) or\
                grid[dy+y][dx+x] != 1: continue
            res += 1+search(grid,y+dy,x+dx)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
