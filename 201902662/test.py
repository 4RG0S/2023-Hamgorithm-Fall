import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

time = 0
air = []
# air에 테두리 부분을 넣는다.
for i in range(m):
    air.append((0, i))
    air.append((n-1, i))
    cheese[0][i] = 2
    cheese[n-1][i] = 2
        
for i in range(1, n-1):
    air.append((i, 0))
    air.append((i, m-1))
    cheese[i][0] = 2
    cheese[i][m-1] = 2

# 더 이상 녹아 없어진 부분이 없을때 까지 반복한다.
while air:
    
    # 외부 공간과 닿은 치즈 저장
    que = []
    while air:
        x, y = air.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if cheese[nx][ny] == 1:
                    que.append((nx, ny))
                elif cheese[nx][ny] == 0:
                    air.append((nx, ny))
                    cheese[nx][ny] = 2

    melt = []
    # 외부 공간과 닿은 치즈 중 2변 이상 닿은 치즈 저장
    while que:
        x, y = que.pop()
        s = cheese[x+1][y] + cheese[x-1][y] + cheese[x][y+1] + cheese[x][y-1]
        if s >= 4 and s != 5:
            melt.append((x, y))
            
    # 치즈가 녹은 부분을 표시
    while melt:
        x, y = melt.pop()
        air.append((x, y))
        cheese[x][y] = 2
    
    if not air:
        break
    time += 1

print(time)