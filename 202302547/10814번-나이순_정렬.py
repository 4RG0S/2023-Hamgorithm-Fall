n = int(input())
arr = []

for i in range(n):
   arr.append(input().split())

arr.sort(key=lambda x: int(x[0])) # 나이순으로 정렬

for _ in range(n):
    print(arr[_][0], arr[_][1])   