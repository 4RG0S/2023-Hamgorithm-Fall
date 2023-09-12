from collections import deque
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    miro = [list(map(int, list(input()[0:n]))) for _ in range(m)]
    
    # 부숴야하는 벽의 개수를 저장하는 dist
    dist = [[10000 for _ in range(n)] for _ in range(m)]
    dist[0][0] = 0
    
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    que = deque()
    que.append((0, 0))
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                # 다음에 이동할 자리에 벽이 있다면
                # 현재 자리의 부숴야 하는 벽의 값 + 1
                # 다음 자리가 이전에 방문했던 값보다 작아지면 갱신
                nd = dist[x][y]
                if miro[nx][ny]:
                    nd += 1
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    que.append((nx, ny))
    
    print(dist[m-1][n-1])
    
if __name__ == "__main__":
    main()