import sys
import heapq
input = sys.stdin.readline
inf = float('inf')

def main():
    n, m = map(int, input().split())
    edges = [[inf for _ in range(n+1)] for _ in range(n+1)]
    path = [['-' for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        edges[i][i] = 0
    
    for _ in range(m):
        a, b, v = map(int, input().split())
        if edges[a][b] > v:
            edges[a][b] = v
            edges[b][a] = v
            path[a][b] = b
            path[b][a] = a
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if edges[i][j] > edges[i][k] + edges[k][j]:
                    edges[i][j] = edges[i][k] + edges[k][j]
                    path[i][j] = path[i][k]
    
    for i in range(1, n+1):
        print(*path[i][1:])
    
if __name__ == "__main__":
    main()