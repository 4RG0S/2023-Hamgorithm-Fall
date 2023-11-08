n, m = map(int, input().split())
prices = [list(map(int, input().split())) for _ in range(m)]

package = [p[0] for p in prices]
single = [p[1] for p in prices]
min_package = min(package)
min_single = min(single)

result = min((n // 6 + 1) * min_package, n // 6 * min_package + (n % 6) * min_single, n * min_single)
print(result)
