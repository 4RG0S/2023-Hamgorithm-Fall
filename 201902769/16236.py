from collections import deque
n = int(input())
babyShark = []
babySharkSize = 2
arr = []
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] == 9:
            babyShark = [i, j]
            arr[i][j] = 0

def bfs():
    global babyShark, babySharkSize, arr
    visited = [[False] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    q = deque([babyShark])
    visited[babyShark[0]][babyShark[1]] = True
    fish = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if arr[nx][ny] <= babySharkSize:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
                    if 0 < arr[nx][ny] < babySharkSize:
                        fish.append((distance[nx][ny], nx, ny))

    if not fish:
        return None
    fish.sort()
    return fish[0]

time = 0
eaten = 0

while True:
    result = bfs()
    if result is None:
        break
    dist, x, y = result
    time += dist
    eaten += 1
    arr[x][y] = 0
    babyShark = [x, y]

    if eaten == babySharkSize:
        babySharkSize += 1
        eaten = 0

print(time)
