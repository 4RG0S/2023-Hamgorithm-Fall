n, d = map(int, input().split())
arr = []

for i in range(1, n + 1):
    temp = list(map(int, str(i)))
    arr.extend(temp)

print(arr.count(d))
