import sys

lenth, epo = map(int, sys.stdin.readline().split())
ar = list(map(int, sys.stdin.readline().split()))
s = ar[0]
for i in range(1,len(ar)):
    s = s+ar[i]
    ar[i] = s

for _ in range(epo):
    first, end = map(int, sys.stdin.readline().split())
    if first == 1:
        print(ar[end-1])
    else:
        print(ar[end-1]-ar[first-2])