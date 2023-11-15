x = int(input())
line = 1

while x > line:
    x -= line
    line += 1

if line % 2 == 0:
    a = x
    b = line - x + 1

elif line % 2 == 1:
    a = line - x + 1
    b = x

print("%d/%d" %(a, b))