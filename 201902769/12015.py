import bisect
n=int(input())
arr=list(map(int,input().split()))
stack=[arr[0]]

for i in range(1, n):
    if arr[i] > stack[-1]:
        stack.append(arr[i])
    else:
        idx = bisect.bisect_left(stack, arr[i])
        stack[idx] = arr[i]

print(len(stack))