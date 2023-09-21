while True:
  table = list(map(int, input().split()))
  table.sort()

  if table[0] ^ table[1] ^ table[2] == 0:
    break

  if table[0]**2 + table[1]** 2 == table[2]**2:
    print("right")

  else:
    print("wrong")