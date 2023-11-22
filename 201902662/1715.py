import sys
import heapq
input = sys.stdin.readline

def main():
    n = int(input())
    heap = []
    for _ in range(n):
        heapq.heappush(heap, int(input()))
    
    cnt = 0
    while len(heap) != 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a+b)
        cnt += a+b
        
    print(cnt)
    
if __name__ == "__main__":
    main()