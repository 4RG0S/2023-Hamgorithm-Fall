import math
import sys

input = sys.stdin.readlines

n = int(input())
table = []
calc = []
res = 0

for _ in range(n):
    table.append(int(input()))

for i in range(1, n):
    calc.append(table[i] - table[i-1])

while len(calc) > 1:
    a = calc.pop()
    b = calc.pop()

    calc.append(math.gcd(a, b))

for i in range(1, n):
    res += (table[i] - table[i-1]) // calc[0] - 1

print(res)