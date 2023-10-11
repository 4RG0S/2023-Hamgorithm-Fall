t = int(input())
res = 0

for _ in range(t):
    isGroup = True

    a = list(input())

    while a:
        k = a.pop(0)
        for i in range(len(a)):
            if a[0] == k:
                k = a.pop(0)
            else:
                break
        
        if k in a:
            isGroup = False
            break
        else:
            continue
        
    if isGroup:
        res += 1

print(res)