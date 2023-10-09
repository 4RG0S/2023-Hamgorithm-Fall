Inf = float('inf')

def main():
    n, m = int(input()), int(input())
    city = [[Inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        city[i][i] = 0
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        city[a-1][b-1] = min(city[a-1][b-1], c)
        
    for k in range(n):
        for a in range(n):
            for b in range(n):
                city[a][b] = min(city[a][b], city[a][k] + city[k][b])
                
    for i in range(n):
        for j in range(n):
            if city[i][j] == Inf:
                city[i][j] = 0
            print(city[i][j], end=" ")
        print()
    
if __name__ == "__main__":
    main()