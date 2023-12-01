import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    coin = [int(input()) for _ in range(n)]
    dp = [0 for _ in range(k+1)]
    
    dp[0] = 1
    for c in coin:
        for i in range(c, k+1):
            dp[i] += dp[i - c]
    
    print(dp[k])
    
if __name__ == "__main__":
    main()