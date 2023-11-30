from sys import stdin
from collections import deque

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def bfs(x, y):
	graph[y][x] = 0
	queue = deque()
	queue.append((x, y))
	while queue:
		x, y = queue.popleft()
		for i in range(8):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 1:
				graph[ny][nx] = 0
				queue.append((nx, ny))

while True:
	w, h = map(int, stdin.readline().split())
	if w == h == 0:
		break
	graph = []
	cnt = 0
	for i in range(h):
		graph.append(list(map(int, stdin.readline().split())))
	for y in range(h):
		for x in range(w):
			if graph[y][x] == 1:
				cnt += 1
				bfs(x, y)
	print(cnt)
	