import math
w, h, x, y, p = map(int, input().split())

r = h / 2
x1, y1 = x, y + r
x2, y2 = x + w, y + r

count = 0

for _ in range(p):
  px, py = map(int, input().split())

  d1 = math.sqrt((x1 - px) ** 2 + (y1 - py) ** 2)
  d2 = math.sqrt((x2 - px) ** 2 + (y2 - py) ** 2)

  if d1 <= r or d2 <= r:
    count += 1
  elif x <= px <= x + w and y <= py <= y + h:
    count += 1

print(count)