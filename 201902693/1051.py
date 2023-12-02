n, m = map(int, input().split())

lst = []
for i in range(n):
    lst.append(list(input()))

answer = 0
for i in range(n):
    for j in range(m):
        for k in range(min(n, m)):
            if ((i + k) < n) and ((j + k) < m) and (lst[i][j] == lst[i][j + k] == lst[i + k][j] == lst[i + k][j + k]):
                answer = max(answer, (k + 1)**2)
                
print(answer)