n, m = map(int, input().split())
chess = []
result = []

for _ in range(n) :
    chess.append(input())

for i in range(n - 7) :
    for j in range(m - 7) :
        temp1 = 0
        temp2 = 0
        
        for a in range(i, i + 8) :
            for b in  range(j, j + 8) :
                if (a + b) % 2 == 0 :
                    if chess[a][b] != 'B':
                        temp1 += 1
                    if chess[a][b] != 'W':
                        temp2 += 1
                else :
                    if chess[a][b] != 'W':
                        temp1 += 1
                    if chess[a][b] != 'B':
                        temp2 += 1
        
        result.append(temp1)
        result.append(temp2)

print(min(result))