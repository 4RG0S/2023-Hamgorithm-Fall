import sys
import heapq
input = sys.stdin.readline

def main():
    n = int(input())
    dic = [[] for _ in range(10001)]
    for _ in range(n):
        d, p = map(int, input().split())
        dic[p].append(d)
        
    heap = []
    cnt = 0
    for i in range(10000, 0, -1):
        for e in dic[i]:
            heapq.heappush(heap, -e)
        if heap:
            cnt += heapq.heappop(heap)        
    print(-cnt)
        
if __name__ == "__main__":
    main()