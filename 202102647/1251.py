a = list(map(str,input()))
save = []
for i in range (1,len(a) -1):
    for j in range(i+1, len(a)):
        f = a[:i]
        s = a[i:j]
        t = a[j:]
        f.reverse()
        s.reverse()
        t.reverse()
        save.append("".join(f+s+t))
print(min(save))
