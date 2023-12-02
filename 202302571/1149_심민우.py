import sys
input = sys.stdin.readline

house = [[0] * 3 for i in range(1001)]

n = int(input())
for i in range(n):
    house[i] = list(map(int,input().split()))

dp = [[0]*3 for i in range(1001)] 
dp[0][0] = house[0][0]
dp[0][1] = house[0][1]
dp[0][2] = house[0][2]

for i in range(1,n):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + house[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + house[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + house[i][2]

print(min(dp[n-1][0],min(dp[n-1][1],dp[n-1][2])))  