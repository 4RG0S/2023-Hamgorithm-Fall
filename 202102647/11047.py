# 그리디 알고리즘
import sys
n, k = map(int,sys.stdin.readline().split())
a = []
for _ in range (n):
    a.append(int(sys.stdin.readline()))
coin = reversed(a)
answer = 0
for i in coin:
    answer += k//i
    k = k % i
print(answer) 