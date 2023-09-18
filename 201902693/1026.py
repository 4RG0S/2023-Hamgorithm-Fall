n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = []
a.sort()
b.sort(reverse=True)

for i in range(n) :
    result.append(a[i] * b[i])
print(sum(result))