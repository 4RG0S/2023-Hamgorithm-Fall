import heapq
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())
    
    visit = [[True for _ in range(m)] for _ in range(n)]
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    que = []
    for i in range(m):
        heapq.heappush(que, (-field[0][i], 0, i))
        visit[0][i] = False
    for i in range(1, n-1):
        heapq.heappush(que, (-field[i][0], i, 0))
        visit[i][0] = False
    if n > 1:
        for i in range(m):
            heapq.heappush(que, (-field[n-1][i], n-1, i))
            visit[n-1][i] = False
    if m > 1:
        for i in range(1, n-1):
            heapq.heappush(que, (-field[i][m-1], i, m-1))
            visit[i][m-1] = False
        
    for _ in range(k):
        v, x, y = heapq.heappop(que)
        print(x+1, y+1)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny]:
                heapq.heappush(que, (-field[nx][ny], nx, ny))
                visit[nx][ny] = False
    
if __name__ == "__main__":
    main()