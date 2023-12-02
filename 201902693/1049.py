n, m = map(int, input().split())
package = []
single = []

for _ in range(m):
    a, b = map(int, input().split())
    package.append(a)
    single.append(b)

min_package = min(package)

answer = 0
while n > 0:
    if n >= 6:
        min_single = min(single) * 6
        n -= 6
    else:
        min_single = min(single) * n
        n = 0
    if min_single < min_package:
        answer += min_single
    else:
        answer += min_package

print(answer)