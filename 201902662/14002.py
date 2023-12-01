def main():
    n = int(input())
    s = list(map(int, input().split()))
    
    up = [1 for _ in range(n)]
    prev = [i for i in range(n)]
    
    for i in range(n):
        for j in range(i+1, n):
            if s[i] < s[j] and up[i] >= up[j]:
                up[j] = up[i]+1
                prev[j] = i
    
    m, child = 1, 0
    for i in range(1, n):
        if m < up[i]:
            m = up[i]
            child = i
    
    path = []
    for i in range(child, -1, -1):
        if i == child:
            path.append(s[i])
            child = prev[i]
    
    print(m)
    print(*path[::-1])
    
if __name__ == "__main__":
    main()