x = int(input())
temp = [64, 32, 16, 8, 4, 2, 1]
count = 0
for i in range(len(temp)):
    if x >= temp[i]:
        count += 1
        x -= temp[i]
    if x == 0:
        break

print(count)