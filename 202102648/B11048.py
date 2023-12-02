n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*m for _ in range(n)]
dp[0][0] = maze[0][0]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + maze[i][0]
for i in range(1, m):
    dp[0][i] = dp[0][i-1] + maze[0][i]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + maze[i][j]

print(dp[n-1][m-1])
