n, m = map(int, input().split())
pack = []
each = []

for _ in range(m):
    a, b = map(int, input().split())

    pack.append(a)
    each.append(b)

pack.sort()
each.sort()

if pack[0] > each[0] * 6:
    print(n * each[0])

else:
    if pack[0] > each[0] * (n % 6):
      print(pack[0] * (n // 6) + each[0] * (n % 6))

    else:
      print(pack[0] * (n // 6) + pack[0])