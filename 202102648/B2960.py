n, k = map(int, input().split())

lst = [0]*(n+1)
cnt=0

for i in range(2, n+1):
    if lst[i]==0:
        for j in range(i, n+1, i):
            if lst[j]==0:
                lst[j]=1
                cnt+=1
                if cnt==k:
                    print(j)
                    break

