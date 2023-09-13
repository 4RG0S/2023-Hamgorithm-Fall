import heapq

n = int(input())
c = [list(map(int, input().split())) for _ in range(n)]

c.sort(key=lambda x: x[0])

# hq
hq = [c[0][1]] 

for i in range(1, len(c)):
    if c[i][0] >= hq[0]:
        heapq.heappop(hq)
    
    heapq.heappush(hq, c[i][1])

print(len(hq))
