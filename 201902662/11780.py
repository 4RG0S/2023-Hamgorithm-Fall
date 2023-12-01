import sys
input = sys.stdin.readline
Inf = 10000000

n, m = int(input()), int(input())
dist = [[Inf for _ in range(n)] for _ in range(n)]
path = [[-1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    if dist[a][b] > c:
        dist[a][b] = c
        path[a][b] = b

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                path[i][j] = path[i][k]

for i in range(n):
    for j in range(n):
        if dist[i][j] == Inf:
            dist[i][j] = 0
        
for i in dist:
    print(*i)

for i in range(n):
    for j in range(n):
        if not dist[i][j]:
            print(0)
            continue
        
        p, s = [i+1], i
        while s != j:
            s = path[s][j]
            p.append(s+1)

        print(len(p), *p)