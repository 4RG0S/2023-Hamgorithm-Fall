import sys
import heapq
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(n)]
    info.sort()
    
    bag = [int(input()) for _ in range(k)]
    bag.sort()
    
    heap = []
    idx, value = 0, 0
    for c in bag:
        while idx < n and info[idx][0] <= c:
            heapq.heappush(heap, -info[idx][1])
            idx += 1
        if heap:
            value += heapq.heappop(heap)
    print(-value)
    
if __name__ == "__main__":
    main()