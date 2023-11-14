import queue
m, n, h = map(int, input().split())
arr = []
tomato = queue.Queue()
visit = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

for z in range(h):
    xy = []
    for y in range(n):
        x = list(map(int, input().split()))
        xy.append(x)
        for i in range(m):
            if x[i] == 1:
                tomato.put((z, y, i))
                visit[z][y][i] = 1
    arr.append(xy)

def dfs():
    while tomato.empty() == False:
        z, y, x = tomato.get()
        dz = [0, 0, 0, 0, 1, -1]
        dy = [0, 0, 1, -1, 0, 0]
        dx = [1, -1, 0, 0, 0, 0]

        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:


                if visit[nz][ny][nx] != 0:
                    continue

                if arr[nz][ny][nx] == 0:
                    visit[nz][ny][nx] = visit[z][y][x] + 1
                    tomato.put((nz, ny, nx))

dfs()
result = 0
flag = True
for z in range(h):
    for y in range(n):
        for x in range(m):
            result = max(result, visit[z][y][x])
            if visit[z][y][x] == 0 and arr[z][y][x] == 0:
                flag = False
if flag:
    print(result - 1)
else:
    print(-1)