import sys

num = int(sys.stdin.readline())

ar = []
for i in range(num):
    ar.append(0)

for j in range(num):
    ar[j] = list(map(int, sys.stdin.readline().split()))

for k in range(1, num):
    ar[k][0] = min(ar[k-1][1], ar[k-1][2]) + ar[k][0]
    ar[k][1] = min(ar[k-1][0], ar[k-1][2])+ ar[k][1]
    ar[k][2] = min(ar[k-1][1], ar[k-1][0]) + ar[k][2]
print(min(ar[num-1][0], ar[num-1][1], ar[num-1][2]))

