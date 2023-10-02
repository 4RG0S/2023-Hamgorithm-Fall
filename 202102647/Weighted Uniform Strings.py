#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    before = ''
    weight = set()
    weighsum = 0
    answer = []
    alpha = dict()
    for i in range (26):
        alpha[chr(97+i)]=(i+1)
    for i in s:
        if i == before:
            weighsum+=alpha[i]
            weight.add(weighsum)
        else:
            weighsum = alpha[i]
            before = i
            weight.add(alpha[i])
    for i in queries:
        if(i in weight):
            answer.append("Yes")
        else:
            answer.append("No")
    return answer



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
