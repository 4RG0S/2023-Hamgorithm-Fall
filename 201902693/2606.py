from collections import deque

n = int(input())
m = int(input())
visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
visited[1] = 1
while q:
    x = q.popleft()
    for i in graph[x] :
        if visited[i] == 0 :
            q.append(i)
            visited[i] = 1
            
print(sum(visited) - 1)