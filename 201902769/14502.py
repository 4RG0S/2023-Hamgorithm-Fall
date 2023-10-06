from itertools import combinations

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def bfs(arr, walls):
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    
    new_arr = [row.copy() for row in arr]
    for x, y in walls:
        new_arr[x][y] = 1
    
    stack = [(i, j) for i in range(n) for j in range(m) if new_arr[i][j] == 2]
    
    while stack:
        x, y = stack.pop()
        for dxi, dyi in zip(dx, dy):
            nx, ny = x + dxi, y + dyi
            if 0 <= nx < n and 0 <= ny < m and new_arr[nx][ny] == 0:
                new_arr[nx][ny] = 2
                stack.append((nx, ny))

    return sum(row.count(0) for row in new_arr)

empty_cells = [(i, j) for i in range(n) for j in range(m) if arr[i][j] == 0]
result = 0

for walls in combinations(empty_cells, 3):
    result = max(result, bfs(arr, walls))

print(result)
