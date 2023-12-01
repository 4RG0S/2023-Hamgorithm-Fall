import sys
input = sys.stdin.readline
Inf = float('inf')

def main():
    n, m, r = map(int, input().split())
    items = list(map(int, input().split()))
    dist = [[Inf for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0 
    
    for _ in range(r):
        a, b, l = map(int, input().split())
        a, b = a-1, b-1
        dist[a][b] = l
        dist[b][a] = l
        
    for k in range(n):
        for a in range(n):
            for b in range(n):
                dist[a][b] = min(dist[a][b], dist[a][k]+dist[k][b])
                
    ans = 0
    for a in range(n):
        cnt = 0
        for b in range(n):
            if dist[a][b] <= m:
                cnt += items[b]
        ans = max(ans, cnt)
    
    print(ans)
    
if __name__ == "__main__":
    main()