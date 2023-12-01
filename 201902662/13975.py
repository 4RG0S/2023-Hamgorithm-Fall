import sys
import heapq
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        k = int(input())
        heap = []
        
        cnt = 0
        for e in list(map(int, input().split())):
            heapq.heappush(heap, e)
            
        while len(heap) != 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            heapq.heappush(heap, a+b)
            cnt += a+b
        
        print(cnt)
    
if __name__ == "__main__":
    main()