import sys
input = sys.stdin.readline

arr = [[0 for _ in range(501)]for _ in range(501)]
dp = [[0 for _ in range(501)]for _ in range(501)]

n = int(input())
for i in range(n):
    arr[i] = list(map(int, input().split()))

dp[0][0] = arr[0][0]
for i in range(1,n):
    for j in range(i+1):
        if j==0:
            dp[i][j] = dp[i-1][j]
        elif i==j:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
        dp[i][j] += arr[i][j]

print(max(dp[n-1]))