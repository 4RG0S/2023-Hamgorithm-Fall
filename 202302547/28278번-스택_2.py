import sys

input = sys.stdin.readline
n = int(input())
stack = []

for _ in range(n):
    temp = input().rstrip() # rstrip() is necessary to remove '\n' at the end of the line
    
    if temp[0] == '1':
        stack.append(int(temp[2:]))
    elif temp == '2':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif temp == '3':
        print(len(stack))
    elif temp == '4':
        if not stack:
            print(1)
        else:
            print(0)
    elif temp == '5':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
