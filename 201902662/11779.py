import heapq
import sys
input = sys.stdin.readline

def main():
    n, m = int(input()), int(input())
    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges[a].append((b, c))
    s, e = map(int, input().split())
    
    parent = [0 for _ in range(n+1)]
    dist = [float('inf') for _ in range(n+1)]
    dist[s] = 0
    
    que = [(0, s)]
    while que:
        d, p = heapq.heappop(que)
        if dist[p] < d:
            continue
        for c, w in edges[p]:
            if dist[c] > d + w:
                parent[c] = p
                dist[c] = d + w
                heapq.heappush(que, (dist[c], c))
    print(dist[e])
    
    route = [e]
    while s != e:
        route.append(parent[e])
        e = parent[e]
    print(len(route))
    print(*route[::-1])
    
if __name__ == "__main__":
    main()