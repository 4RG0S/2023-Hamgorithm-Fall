n = int(input())
arr = list(map(int, input().split()))
stack = []
num = 1

for i in range(len(arr)):
    if arr[i] == num:
        num += 1
    else:
        while stack and stack[-1] == num:
            stack.pop()
            num += 1
        if not stack or arr[i] < stack[-1]:
            stack.append(arr[i])
        else:
            break

for i in range(len(stack)):
    if stack[-1] == num:
        stack.pop()
        num += 1
    else:
        print("Sad")
        break

if not stack:
    print("Nice")