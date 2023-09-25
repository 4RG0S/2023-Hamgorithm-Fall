import sys
input = sys.stdin.readline

n = int(input())
table = []

for _ in range(n):
  a = list(input().split())

  if a[0] == "push_front":
    table.insert(0, a[1])

  elif a[0] == "push_back":
    table.append(a[1])

  elif a[0] == "pop_front":
    if len(table) != 0:
      print(table.pop(0))
    else:
      print(-1)

  elif a[0] == "pop_back":
    if len(table) != 0:
      print(table.pop())
    else:
      print(-1)

  elif a[0] == "size":
    print(len(table))

  elif a[0] == "empty":
    if len(table) == 0:
      print(1)
    else:
      print(0)

  elif a[0] == "front":
    if len(table) != 0:
      print(table[0])
    else:
      print(-1)

  elif a[0] == "back":
    if len(table) != 0:
      print(table[-1])
    else:
      print(-1)