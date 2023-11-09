from collections import deque
from math import log2
import sys
input = sys.stdin.readline

# 입력
n = int(input())
logN = int(log2(n)+1)

# graph 생성
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# root를 1로 하는 tree 생성
# tree의 깊이 설정
anc = [[0 for _ in range(logN)] for _ in range(n+1)]
val = [[0 for _ in range(logN)] for _ in range(n+1)]
depth = [0 for _ in range(n+1)]

depth[1] = 1
que = deque([1])
while que:
    e = que.pop()
    for a, b in graph[e]:
        if depth[a]:
            continue
        
        anc[a][0] = e
        val[a][0] = b
        depth[a] = depth[e] + 1
        que.append(a)

# tree의 조상 node 설정
# 조상 node까지의 비용 설정
for j in range(1, logN):
    for i in range(1, n+1):
        val[i][j] = val[i][j-1] + val[anc[i][j-1]][j-1]
        anc[i][j] = anc[anc[i][j-1]][j-1]

# 두 노드의 거리 탐색
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    
    # lca 알고리즘
    cost = 0
    if depth[a] < depth[b]:
        a, b = b, a
    
    for i in range(logN-1, -1, -1):
        if depth[anc[a][i]] >= depth[b]:
            cost += val[a][i]
            a = anc[a][i]
    
    if a == b:
        print(cost)
        continue
    
    for i in range(logN-1, -1, -1):
        if anc[a][i] != anc[b][i]:
            cost += val[a][i] + val[b][i]
            a = anc[a][i]
            b = anc[b][i]
    cost += val[a][i] + val[b][i]
    
    print(cost)