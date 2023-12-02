from collections import deque

R, C = map(int, input().split())
board = [input() for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global answer
    queue = deque([(x, y, board[x][y])])
    visited = set([(x, y, board[x][y])])
    answer = 1
    
    while queue:
        x, y, path = queue.popleft()
        answer = max(answer, len(path))
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in path:
                new_state = (nx, ny, path + board[nx][ny])
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append(new_state)

answer = 1
bfs(0, 0)

print(answer)
