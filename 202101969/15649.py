import itertools
from itertools import combinations
import sys

max_num, num = map(int, sys.stdin.readline().split())
ar = []
for i in range(1, max_num+1):
    ar.append(i)
permu = list(itertools.permutations(ar, num))
permu.sort()
for i in permu:
    print(*i)