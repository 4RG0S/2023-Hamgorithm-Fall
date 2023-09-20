import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    dp = [0 for _ in range(k+1)]
    for _ in range(n):
        w, v = map(int, input().split())
        for i in range(k, w-1, -1):
            dp[i] = max(dp[i], dp[i-w]+v)
    print(dp[k])
        
if __name__ == "__main__":
    main()