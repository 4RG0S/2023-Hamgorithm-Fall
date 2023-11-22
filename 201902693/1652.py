n = int(input())

lst = [input().strip() for _ in range(n)]

row, col = 0, 0
for i in range(n) :
  row_count, col_count = 0, 0
  for j in range(n) :
    if lst[i][j] == '.' :
      row_count += 1
    else :
      if row_count > 1 :
        row += 1
      row_count = 0

    if lst[j][i] == '.' :
      col_count += 1
    else :
      if col_count > 1 :
        col += 1
      col_count = 0
  if row_count > 1 :
    row += 1
  if col_count > 1 :
    col += 1

print(row, col)