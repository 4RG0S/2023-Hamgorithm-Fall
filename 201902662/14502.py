from collections import deque
import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(n)]

    # lab의 바이러스와 빈칸의 위치와 개수를 저장한다.
    virus, empty = [], []
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                empty.append((i, j))
            elif lab[i][j] == 2:
                virus.append((i, j))

    cnt, vrs = len(empty), 64
    # lab에 빈칸에 벽을 3개 세운다.
    for i in range(cnt):
        x1, y1 = empty[i]
        lab[x1][y1] = 1
        for j in range(i+1, cnt):
            x2, y2 = empty[j]
            lab[x2][y2] = 1
            for k in range(j+1, cnt):
                x3, y3 = empty[k]
                lab[x3][y3] = 1
    
                # bfs를 통해 연구실의 바이러스를 퍼트려 퍼트려진 바이러스의 개수를 구한다.
                crnt = 0
                visit = [[False for _ in range(m)] for _ in range(n)]
                dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
                
                que = deque(virus)
                while que:
                    x, y = que.popleft()
                    if visit[x][y]:
                        continue
                    visit[x][y] = True
                    crnt += 1
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0 <= nx < n and 0 <= ny < m \
                            and lab[nx][ny] == 0 and not visit[nx][ny]:
                            que.append((nx, ny))
                
                if vrs > crnt:
                    vrs = crnt
    
                lab[x3][y3] = 0
            lab[x2][y2] = 0
        lab[x1][y1] = 0
    
    print(cnt-3-(vrs-len(virus)))
    
if __name__ == "__main__":
    main()