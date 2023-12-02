#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#

def componentsInGraph(gb):
    # Write your code here
    n = len(gb)
    parent = list(range(2 * n + 1))
    rank = [0] * (2 * n + 1)
    reco = [0] * (2 * n + 1)

    def union(a, b):
        A = find(a)
        B = find(b)
        if A != B:
            if rank[A] > rank[B]:
                parent[B] = A
                rank[A] += 1
            else:
                parent[A] = B
                rank[B] += 1

    def find(a):
        if parent[a] == a:
            return a
        parent[a] = find(parent[a])
        return parent[a]

    for a, b in gb:
        union(a, b)

    # Find the sizes of all connected components
    for i in range(1, 2 * n + 1):
        root = find(i)
        reco[root] += 1

    # Find the minimum and maximum sizes of the connected components
    min_size = float('inf')
    max_size = 0
    for i in range(1, 2 * n + 1):
        if reco[i] > 1:
            min_size = min(min_size, reco[i])
            max_size = max(max_size, reco[i])

    return [min_size, max_size]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
