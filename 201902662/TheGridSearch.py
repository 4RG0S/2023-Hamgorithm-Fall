#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(R, C, G, r, c, P):
    for a in range(R-r+1):
        for b in range(C-c+1):
            if G[a][b] != P[0][0]:
                continue
            has = True
            for i in range(r):
                for j in range(c):
                    if G[a+i][b+j] != P[i][j]:
                        has = False
                        break
                if has == False:
                    break
            
            if has:
                return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(R, C, G, r, c, P)

        fptr.write(result + '\n')

    fptr.close()
