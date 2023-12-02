n, m = map(int, input().split())
cnt = 0
max = 0

if n == 0:
    print(0)
    exit()
    
arr = list(map(int, input().split()))

for i in range(len(arr)):
    if max + arr[i] > m:
        cnt += 1
        max = arr[i]
    elif max + arr[i] < m:
        max += arr[i]
    else:
        cnt += 1
        max = 0
        
if max > 0:
    cnt += 1        

print(cnt)