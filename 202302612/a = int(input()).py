a = int(input())
arr = [[0] * 14 for _ in range(14)]

for i in range(a):
    b = int(input())
    c = int(input())
    for j in range(14):
        if i == 0:
            arr[i][j] = j
        elif i == 1:
            arr[i][j] = 1
                
    print(arr[b-1][c-1])