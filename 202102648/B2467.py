n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = n - 1
min_value = abs(arr[left] + arr[right])
ans = (arr[left], arr[right])

while left < right:
    temp = arr[left] + arr[right]
    if abs(temp) < min_value:
        min_value = abs(temp)
        ans = (arr[left], arr[right])
        if temp == 0:
            break

    if temp < 0:
        left += 1
    else:
        right -= 1

print(ans[0], ans[1])
