n, m = map(int, input().split())
table = []
res = []

for _ in range(n):
    table.append(list(input()))

def findans(x, y):
    stWhite = 0
    stBlack = 0

    for k in range(x,x+8):
        for l in range(y,y+8):
            if (k % 2 + l % 2 == 0 or k % 2 + l % 2 ==  2):
                if table[k][l] == 'W':
                    stBlack += 1
                else:
                    stWhite += 1

            else:
                if table[k][l] == 'B':
                    stBlack += 1
                else:
                    stWhite += 1

    return min(stWhite, stBlack)

for i in range(n-7):
    for j in range(m-7):
        res.append(findans(i, j))

res.sort()
print(res[0])