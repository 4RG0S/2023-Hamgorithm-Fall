n, k = map(int, input().split())

lst = [[0, 0]]

for _ in range(n):
    lst.append(list(map(int, input().split())))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j>= lst[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-lst[i][0]] + lst[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])


