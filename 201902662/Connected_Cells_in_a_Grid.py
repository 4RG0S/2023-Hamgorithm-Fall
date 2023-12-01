import sys
input = sys.stdin.readline

dx, dy = [0, 1, 1, 1], [1, 1, 0, -1]
parent, rank = [], []

def find(x):
	if x == parent[x]:
		return x
	parent[x] = find(parent[x])
	return parent[x]

def union(a, b):
	a = find(a)
	b = find(b)
	
	if rank[a] < rank[b]:
		a, b = b, a
	
	parent[b] = a
	if rank[a] == rank[b]:
		rank[a] += 1

def connectedCell(n, m, matrix):
    global parent, rank
    for x in range(n):
        for y in range(m):
            if matrix[x][y]:
                parent.append(m*x+y)
                rank.append(1)
            else:
                parent.append(-1)
                rank.append(0)
    
    for x in range(n):
        for y in range(m):
            if matrix[x][y] == 0:
                continue
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny]:
                    union(m*x+y, m*nx+ny)
    
    cnt = [0 for _ in range(n*m)]
    for x in range(n):
        for y in range(m):
            if matrix[x][y]:
                cnt[find(m*x+y)] += 1
    return max(cnt)

def main():
    n, m = int(input()), int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print(connectedCell(n, m, matrix))
    
if __name__ == "__main__":
    main()