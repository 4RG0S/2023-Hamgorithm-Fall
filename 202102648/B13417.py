t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(input().split())
    ans = [lst.pop(0)]

    for c in lst:
        if c <= ans[0]:
            ans = [c]+ans
        else:
            ans = ans+[c]
            
    st = ""
    for c in ans:
        st += c
    print(st)

