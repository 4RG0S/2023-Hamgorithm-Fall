import sys
input = sys.stdin.readline
max = 1000000

def main():
    n = int(input())
    val = [list(map(int, input().split())) for _ in range(n)]
    ans = max
    
    for i in range(3):
        dp = [[max] * 3 for _ in range(n)]
        dp[0][i]  = val[0][i]
        for j in range(1, n):
            dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + val[j][0]
            dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + val[j][1]
            dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + val[j][2]
        dp[-1][i] = max
        ans = min(ans, min(dp[-1]))
    
    print(ans)
    
if __name__ == "__main__":
    main()