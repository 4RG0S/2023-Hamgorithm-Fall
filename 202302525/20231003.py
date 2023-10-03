table = []

for _ in range(int(input())):
  test = list(input())
  
  if len(table) == 0:
    table = [i for i in test]
  
  else:
    for i in range(len(table)):
      if table[i] != test[i]:
        table[i] = '?'

for i in table:
  print(i, end = '')