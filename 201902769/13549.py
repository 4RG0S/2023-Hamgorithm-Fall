import heapq
import sys
a, b = map(int, input().split())
cost = [sys.maxsize] * 1000001

hq = []
heapq.heappush(hq, (0, a))
cost[a] = 0

while hq:
    t, cur = heapq.heappop(hq)

    if cost[b] != sys.maxsize:
        print(cost[b])
        break

    for next_t, next in [(t+1, cur+1), (t+1, cur-1), (t, cur*2)]:
        if 0 <= next <= 1000000 and cost[next] > next_t:
            cost[next] = next_t
            heapq.heappush(hq, (next_t, next))