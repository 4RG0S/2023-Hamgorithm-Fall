import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ch = [list(map(int, input().split())) for _ in range(n)]

visit = [[0 for _ in range(m)] for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

air = [(0, 0)]
def dfs():
    while air:
        x, y = air.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] != -1:
                if ch[nx][ny]:
                    visit[nx][ny] += 1
                else:
                    air.append((nx, ny))
                    visit[nx][ny] = -1

dfs()
time = 0
while True:                 
    for x in range(n):
        for y in range(m):
            if visit[x][y] > 1:
                air.append((x, y))
                ch[x][y] = 0
                visit[x][y] = -1
                
    if not air:
        break
    time += 1
    
    dfs()

print(time)