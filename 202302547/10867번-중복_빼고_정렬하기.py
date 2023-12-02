n = int(input())
num = set(map(int, input().split()))
for i in range(len(num)):
    print(sorted(num)[i], end=' ')