r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
trace = set()
def dfs(x, y, ans):
    trace.add(board[x][y])
    
    if ans < len(trace):
        ans = len(trace)
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in trace:
            ans = dfs(nx, ny, ans)
    
    trace.remove(board[x][y])
    return ans

print(dfs(0, 0, 0))