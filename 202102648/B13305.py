import sys
input=sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))
c = list(map(int, input().split()))

min_cost = c[0]
ans = min_cost*d[0]

for i in range(1, n-1):
    if c[i]<min_cost:
        min_cost = c[i]
    ans += min_cost * d[i]

print(ans)
