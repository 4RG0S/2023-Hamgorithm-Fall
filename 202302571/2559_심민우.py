from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

ps = [arr[0]] * n
for i in range(1, n):
    ps[i] = ps[i - 1] + arr[i]

maxsum = ps[k - 1]
for i in range(1, n-k+1):
    maxsum = max(maxsum, ps[i + k - 1] - ps[i - 1])

print(maxsum)