string, bomb = input(), input()
bomb = bomb[::-1]

stack = []
for s in string:
    stack.append(s)
    
    if stack[-1] == bomb[0] and len(stack) >= len(bomb):
        sub, has = [], True
        for b in bomb:
            sub.append(stack.pop())
            if sub[-1] != b:
                has = False
                break
        
        if has:
            continue
        stack += reversed(sub)

if stack:
    print(''.join(stack))
else:
    print("FRULA")