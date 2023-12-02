n = int(input())
count = n

for _ in range(n) :
    s = input()
    for i in range(len(s) - 1) :
        if s[i] == s[i + 1] :
            pass
        elif s[i] in s[i + 1 :] :
            count -= 1
            break

print(count)