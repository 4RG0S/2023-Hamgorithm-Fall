import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    
    n = int(input())
    parent, rank = {}, {}
    
    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x, y = find(x), find(y)
        
        if x != y:
            parent[x] = y
            temp = rank[x] + rank[y]
            rank[x] = temp
            rank[y] = temp
    
    for _ in range(n):
        a, b = input().split()
        
        if a not in parent.keys():
            parent[a] = a
            rank[a] = 1
        
        if b not in parent.keys():
            parent[b] = b
            rank[b] = 1
        
        union(a, b)
        
        print(rank[find(a)])