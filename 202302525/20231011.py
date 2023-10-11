n, m = map(int, input().split())

table = [0 for _ in range(n)]

for _ in range(m):
    i, j, k = map(int,input().split())

    for l in range(i-1, j):
        table[l] = k

print(*table)