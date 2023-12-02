from sys import *
input = stdin.readline

n = int(input())
budget = list(map(int, input().split()))
m = int(input())
budget.sort()

l, r=0,budget[-1]
maxb = 0

while l<=r:
    mid = (l+r)//2
    sum, i=0,0
    for t in budget:
        if t >= mid:
            break
        sum += t
        i+=1
    sum += (len(budget) - i) * mid
    if sum <= m:
        l = mid+1
        maxb = max(mid,maxb)
    else:
        r = mid-1

print(maxb)

