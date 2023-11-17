n, k = map(int, input().split())
arr1 = [] * n
arr2 = [0] * n
money = 0

for i in range(n):
    arr1.append(int(input()))

for i in range(len(arr1)-1, -1, -1):
    arr2[i] = (k - money) // arr1[i]
    money += arr2[i] * arr1[i]
    
print(sum(arr2))