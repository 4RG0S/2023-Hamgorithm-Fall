import sys
sys.setrecursionlimit(10 ** 8)

def dfs(x, y):
    if x==m-1 and y==n-1:
        return 1
    
    if dp[x][y] == -1:
        dp[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[x][y] > graph[nx][ny]:
                    dp[x][y] += dfs(nx, ny)

    return dp[x][y]

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
print(dfs(0, 0))
