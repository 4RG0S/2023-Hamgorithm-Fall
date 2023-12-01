def main():
    n = int(input())
    s = list(map(int, input().split()))
    
    up, down = [1]*n, [1]*n
    
    for i in range(n):
        for j in range(i+1, n):
            if s[i] < s[j] and up[i] >= up[j]:
                up[j] = up[i]+1
    
    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):
            if s[i] < s[j] and down[i] >= down[j]:
                down[j] = down[i]+1
    
    m = 0
    for i in range(n):
        m = max(m, up[i]+down[i]-1)
    print(m)
    
if __name__ == "__main__":
    main()