import sys
a,b = map(int,sys.stdin.readline().split())
# 높이 a , 너비 b
block = list(map(int,sys.stdin.readline().split()))
count = 0
for i in range (1, b-1):
    l_max = max(block[:i])
    r_max = max(block[i+1:])

    least = min(l_max,r_max)
    if block[i] < least:
        count += least - block[i]

print(count)