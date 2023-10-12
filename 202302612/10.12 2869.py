a, b, v = map(int, input().split())
cnt = 0
d = 0
while cnt <= v:
    cnt += a
    if cnt > v:
        break
    cnt -= b
    d += 1
print(d)
