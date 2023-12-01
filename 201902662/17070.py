def main():
    n = int(input())
    home = [[0 for _ in range(n+1)]]
    for _ in range(n):
        home.append([0]+list(map(int, input().split())))
    
    # dp배열에 가로, 세로, 대각선 방향으로 갈 수 있는 방법들 저장
    dp = [[[0, 0, 0] for _ in range(n+1)] for _ in range(n+1)]
    dp[1][2][0] = 1
    
    # 1번째 행 초기화
    for i in range(3, n+1):
        if home[1][i]:
            continue
        dp[1][i][0] = dp[1][i-1][0]
    
    # 2번째 행부터 이전행을 바탕으로 구한다.
    for i in range(2, n+1):
        for j in range(1, n+1):
            if home[i][j]:
                continue
            
            # 가로
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            
            # 세로
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
            
            # 대각선
            if home[i-1][j] or home[i][j-1]:
                continue
            dp[i][j][2] = sum(dp[i-1][j-1])

    print(sum(dp[n][n]))
    
if __name__ == "__main__":
    main()