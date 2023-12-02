n = int(input())
arr = []

for _ in range(n):
    arr.append(input().strip())

# arr = sorted(set(arr))
arr = sorted(set(arr), key=lambda x: (len(x), x))

# for i in range(50):
#     for j in range(len(arr)):
#         if len(arr[j]) == i:
#             print(arr[j])
#         else:
#             continue

for _ in range(len(arr)):
    print(arr.pop(0))