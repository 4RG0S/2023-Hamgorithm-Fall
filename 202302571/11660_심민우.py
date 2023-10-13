import sys
input = sys.stdin.readline

n, m = map(int,input().split())

asum = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    arr = list(map(int,input().split()))
    asum[i][1] = arr[0]
    for j in range(2,n+1):
        asum[i][j] = arr[j-1] + asum[i][j-1]


for _ in range(m):
    y1,x1,y2,x2 = map(int,input().split())
    ans = 0
    for i in range(y1,y2+1):
        ans += asum[i][x2] - asum[i][x1-1]
    print(ans)