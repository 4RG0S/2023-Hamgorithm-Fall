import sys

input = sys.stdin.readline
n = int(input())
stack = []

for _ in range(n):
    temp = int(input())
    if temp == 0:
        stack.pop()
    else:
        stack.append(temp)

print(sum(stack))
    