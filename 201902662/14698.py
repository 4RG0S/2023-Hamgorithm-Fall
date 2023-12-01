import sys
import heapq
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        li = list(map(int, input().split()))
        
        heap = []
        for e in li:
            heapq.heappush(heap, e)

        cost = 1
        while len(heap) != 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            heapq.heappush(heap, a*b)
            cost = (cost*a*b)%1000000007
        print(cost)
    
if __name__ == "__main__":
    main()