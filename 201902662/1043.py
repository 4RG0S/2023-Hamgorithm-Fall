def main():
    n, m = map(int, input().split())
    
    parent = [i for i in range(n+1)]
    rank = [1 for _ in range(n+1)]
    
    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a, b = find(a), find(b)
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
    
    p = 0
    io = list(map(int, input().split()))
    if io[0] > 0:
        p = io[1]
    for i in range(io[0], 1, -1):
        union(p, io[i])
    
    io = [list(map(int, input().split())) for _ in range(m)]
    for i in range(m):
        a = io[i][1]
        for j in range(io[i][0], 1, -1):
            union(a, io[i][j])
    
    cnt = 0
    for i in range(m):
        attend = True
        for j in range(io[i][0], 0, -1):
            if find(io[i][j]) == find(p):
                attend = False
        if attend:
            cnt += 1
    print(cnt)
        
if __name__ == "__main__":
    main()