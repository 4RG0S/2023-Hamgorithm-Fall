n = int(input())
r = [int(input()) for _ in range(n)]

r.sort(reverse=True)

max_weight = 0
for i in range(n):
    max_weight = max(max_weight, r[i] * (i + 1))

print(max_weight)
