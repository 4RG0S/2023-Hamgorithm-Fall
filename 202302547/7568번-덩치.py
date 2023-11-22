n = int(input())
arr = [0] * n
rank = [1] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))
    
for i in range(n):
    for j in range(n):
        if arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
            continue
        elif arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank[i] += 1
        else:
            continue

print(*rank)