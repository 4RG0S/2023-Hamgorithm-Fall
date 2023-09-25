n = int(input())
arr = list(str(n))
arr.sort(reverse=True)
for i in range(len(arr)):
    print(arr[i], end='')