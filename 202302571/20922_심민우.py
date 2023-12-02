from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = [0] * 100001
cnt[arr[0]] = 1

s, e = 0,0
maxlen = 0
while not (s>e):
    if cnt[arr[e]] > k:
        cnt[arr[s]] -= 1
        s += 1
        maxlen = max(maxlen, e - s + 1)
    else:
        if e == n-1:
            maxlen = max(maxlen, e - s + 1)
            break
        else:
            e+=1
            cnt[arr[e]] += 1

print(maxlen)