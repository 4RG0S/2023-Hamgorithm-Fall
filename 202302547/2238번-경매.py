U, N = map(int, input().split())
arr = [[] for _ in range(10001)]
cnt = [0] * 10001
m = 10001

for i in range(N):
    name, price = input().split()
    price = int(price)
    arr[price].append(name)
    cnt[price] += 1
    
for i in range(10001): 
    if cnt[i] != 0:  
        m = min(cnt[i],m)

for i in range(10001):
    if m == cnt[i]:
        print(arr[i][0],i)
        break
