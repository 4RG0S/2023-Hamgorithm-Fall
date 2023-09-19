import sys
from collections import deque
a,b = map(int,sys.stdin.readline().split())
graph = []
count = 0
for _ in range (a):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):

    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range (4):
            _x = x+dx[i]
            _y = y +dy[i]
            if 0<= _x <a and 0<=_y<b and graph[_x][_y] ==1:
                queue.append((_x,_y))
                graph[_x][_y] = graph[x][y] +1

    return graph[a-1][b-1]


print(bfs(0,0))