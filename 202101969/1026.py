import sys
num = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort()
b.sort(reverse=True)
s =0
for i in range(num):
    s += a[i]*b[i]
print(s)