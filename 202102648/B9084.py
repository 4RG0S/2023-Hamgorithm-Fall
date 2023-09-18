import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    m = int(input())

    dp = [0 for _ in range(m+1)]
    dp[0] = 1

    for i in lst:
        for j in range(i, m+1):
            dp[j] += dp[j-i]
    
    print(dp[m])
