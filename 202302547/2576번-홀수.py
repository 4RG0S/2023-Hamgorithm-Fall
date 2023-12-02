arr = []

for _ in range(7):
    temp = int(input())
    if temp % 2 == 1:
        arr.append(temp)

if not arr:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))