import sys
import heapq
input = sys.stdin.readline
Inf = float('inf')

def main():
    n, m = map(int, input().split())
    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges[a].append((b, c))
        edges[b].append((a, c))
        
    dist = [Inf for _ in range(n+1)]
    dist[1] = 0
    
    que = [(0, 1)]
    while que:
        d, p = heapq.heappop(que)
        if dist[p] < d: continue
        for c, w in edges[p]:
            if dist[c] > d + w:
                dist[c] = d + w
                heapq.heappush(que, (dist[c], c))
    print(dist[n])
    
if __name__ == "__main__":
    main()