import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    
    parent = [i for i in range(n+1)]
    rank = [1 for _ in range(n+1)]
    
    def union(a, b):
        a, b = find(a), find(b)
        
        if rank[a] < rank[b]:
            a, b = b, a
        
        parent[b] = a
        if rank[b] == rank[b]:
            rank[a] += 1
    
    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    
    for _ in range(m):
        op, a, b = map(int, input().split())
        
        if op:
            if find(a) == find(b):
                print("yes")
            else:
                print("no")
        else:
            union(a, b)
    
if __name__ == "__main__":
    main()