s = input()
b = input()

sstack = []
for i in range(len(s)):
    sstack.append(s[i])
    if len(sstack) >= len(b):
        tmp = "".join(sstack[-len(b):])
        if tmp == b:
            for _ in range(len(b)):
                sstack.pop()


ans = ""
if len(sstack) == 0:
    print("FRULA")
else:
    print("".join(sstack))