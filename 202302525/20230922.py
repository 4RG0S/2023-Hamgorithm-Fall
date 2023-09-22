import math

n = int(input())
table = []
result = 0

if n == 0:
  print(0)

else:
  for _ in range(n):
    table.append(int(input()))

  table.sort()

  k = math.floor(n * 15 / 100 + 0.5)

  for i in range(n - 2 * k):
    result += table[i+k]

  print(math.floor(result / (n - 2 * k) + 0.5))