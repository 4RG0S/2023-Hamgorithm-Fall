str = input()
n = int(input())
arr = []
count = 0

for _ in range(n):
    temp = input() * 2
    arr.append(temp)
    if str in temp:
        count += 1

print(count)