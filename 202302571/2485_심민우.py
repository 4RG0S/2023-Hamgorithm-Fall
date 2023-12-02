import math
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * n
arr[0] = int(input())
dis = []
for i in range(1,n):
    arr[i] = int(input())
    dis.append(arr[i] - arr[i-1])

x = dis[0]
for i in dis:
    x = math.gcd(x,i)

ans = 0
for i in dis:
    ans += i // x - 1

print(ans)