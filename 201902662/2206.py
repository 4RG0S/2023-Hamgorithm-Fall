from collections import deque
import sys
input = sys.stdin.readline
Inf = float('inf')

def main():
    n, m = map(int, input().split())
    matrix = [input() for _ in range(n)]
    
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    # 1. 벽을 부수지 않고 갈 수 있는 최단거리, 2. 벽을 부수고 갈 수 있는 최단거리
    dist = [[[Inf, Inf] for _ in range(m)] for _ in range(n)]
    dist[0][0] = [1, Inf]
    
    que = deque([(0, 0)])
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == '1':
                    if  dist[x][y][0]+1 < dist[nx][ny][1]:
                        dist[nx][ny][1] = dist[x][y][0]+1
                        que.append((nx, ny))
                else:
                    renew = False
                    if dist[x][y][0]+1 < dist[nx][ny][0]:
                        dist[nx][ny][0] = dist[x][y][0]+1
                        renew = True
                    
                    if dist[x][y][1]+1 < dist[nx][ny][1]:
                        dist[nx][ny][1] = dist[x][y][1]+1
                        renew = True
                        
                    if renew:
                        que.append((nx, ny))
    
    result = min(dist[n-1][m-1])
    if result == Inf:
        print(-1)
    else:
        print(result)
    
if __name__ == "__main__":
    main()