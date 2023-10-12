import sys
input = sys.stdin.readline

def bellman_ford(n, graph, start):
    dist = [100000 for _ in range(n+1)]
    dist[start] = 0
    
    # edge를 1개부터 n-1개까지 써서 갈 수 있는 노드를 방문
    # 거리를 비교해서 최단 거리를 갱신한다.
    for _ in range(n-1):
        for s in range(1, n+1):
            for e, t in graph[s]:
                if dist[e] > dist[s] + t:
                    dist[e] = dist[s] + t
    
    # 한번 더 순회하여 값이 작아지면 음수 사이클이 존재
    for s in range(1, n+1):
        for e, t in graph[s]:
            if dist[e] > dist[s] + t:
                return 1   
    return 0

def main():
    t = int(input())
    for _ in range(t):
        n, m, w = map(int, input().split())
        graph = [[] for _ in range(n+1)]
        for _ in range(m):
            s, e, t = map(int, input().split())
            graph[s].append((e, t))
            graph[e].append((s, t))
        for _ in range(w):
            s, e, t = map(int, input().split())
            graph[s].append((e, -t))
            
        if bellman_ford(n, graph, 1):
            print("YES")
        else:
            print("NO")
    
if __name__ == "__main__":
    main()