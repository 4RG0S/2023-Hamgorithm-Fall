import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        
        # tree 생성
        tree = [0 for i in range(n+1)]
        for _ in range(n-1):
            a, b = map(int, input().split())
            tree[b] = a
        
        # 조상 node 탐색
        a, b = map(int, input().split())
        
        pa, pb = [0, a], [0, b]
        
        while tree[a]:
            pa.append(tree[a])
            a = tree[a]
        
        while tree[b]:
            pb.append(tree[b])
            b = tree[b]

        result = 0
        while True:
            a, b = pa.pop(), pb.pop()
            if a != b:
                break
            result = a
        
        print(result)
    
if __name__ == "__main__":
    main()