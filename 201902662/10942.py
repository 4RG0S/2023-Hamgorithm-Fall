import sys
input = sys.stdin.readline

def main():
    n = int(input())
    pal = [0] + list(map(int, input().split()))
    
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        dp[i][i] = 1
    
    for i in range(1, n):
        if pal[i] == pal[i+1]:
            dp[i][i+1] = 1
    
    for e in range(2, n):
        for s in range(1, n-e+1):
            if dp[s+1][s+e-1] and pal[s] == pal[s+e]:
                dp[s][s+e] = 1    
    
    m = int(input())
    for _ in range(m):
        s, e = map(int, input().split())
        print(dp[s][e])
    
if __name__ == "__main__":
    main()