import sys

h, s = map(int, sys.stdin.readline().split())
ar = [int(sys.stdin.readline()) for _ in range(h)]

# 이진탐색 r
ar.sort()
chai = ar[-1] - ar[0]
start, end = 1, chai

re = 0

while start <= end:
    mid = (start + end)//2
    current = ar[0]
    c = 1
    dif = chai

    for i in range(1, h):
        if ar[i] - current >= mid:
            dif = min(dif, ar[i]-current)
            c +=1
            current = ar[i]
    if c >= s:
        start = mid+1
        re = max(re, dif)
    else:
        end = mid -1
print(re)