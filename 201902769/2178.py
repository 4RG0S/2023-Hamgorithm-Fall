import queue
a, b = map(int, input().split())
arr = []
for i in range(a):
    arr.append([int(i) for i in input()])

def bfs():
    q = queue.Queue()
    q.put([0, 0])
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    visited = [[False] * b for _ in range(a)]

    while not q.empty():
        y, x = q.get()
        if y == a - 1 and x == b - 1:
            return arr[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < a and 0 <= nx < b and arr[ny][nx] == 1:
                visited[ny][nx] = True
                q.put([ny, nx])
                arr[ny][nx] = arr[y][x] + 1
    


print(bfs())
# print(arr)