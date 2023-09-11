import sys
sys.setrecursionlimit(10**5)
# DFS 사용 : 깊이 우선 탐색 = Stack
n, m, k = map(int, sys.stdin.readline().split())
gate = [[0 for i in range(m)] for j in range(n)]
for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    gate[r-1][c-1] = 1
visit = [[False for i in range(m)] for _ in range(n)]
dx = [0, 0, -1, 1]  # 좌우상하
dy = [-1, 1, 0, 0]  # 좌우상하

answer = 0

# DFS 시작


def DFS(x, y):
    global count
    for i in range(4):
        _x = x + dx[i]
        _y = y + dy[i]
        if _x >= 0 and _x < n and _y >= 0 and _y < m:
            # 범위 내에서 주변에 쓰레기 인게 있고, 방문한 적 없으면 count+1한 후 해당 좌표에서 DFS를 돌림
            if gate[_x][_y] == 1 and not visit[_x][_y]:
                visit[_x][_y] = True
                count += 1
                DFS(_x, _y)


for i in range(n):
    for j in range(m):
        if gate[i][j] == 1 and not visit[i][j]:
            count = 0
            DFS(i, j)
            answer = max(answer, count)
print(answer)
