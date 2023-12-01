from collections import deque
import sys
input = sys.stdin.readline

def main():
    v = int(input())
    
    # 입력에 맞는 tree 생성
    tree = {i:{} for i in range(1, v+1)}
    for _ in range(v):
        line = list(map(int, input().split()))
        vertex = line[0]
        for key in range(1, len(line)//2):
            neighbor, value = line[2*key-1], line[2*key]
            tree[vertex][neighbor] = value
    
    # tree에서 지름이 최대가 되도록하는 node와 최대 지름을 찾는 dfs 알고리즘
    def dfs(start_node):
        max_node = 0
        max_length = 0

        visit = [True for _ in range(v+1)]
        visit[start_node] = False
        
        stack = deque([(start_node, 0)])
        while stack:
            vertex, length = stack.pop()
            for key in tree[vertex].keys():
                if visit[key]:
                    visit[key] = False
                    stack.append((key, length + tree[vertex][key]))
                    if length + tree[vertex][key] > max_length:
                        max_node = key
                        max_length = length + tree[vertex][key]
        
        return max_node, max_length
    
    # 1번 node에서 지름이 최대가 되도록하는 node를 찾는다.
    max_node = dfs(1)[0]
    # 지름이 최대가 되도록하는 node에서 최대 지름을 찾는다.
    max_length = dfs(max_node)[1]
    
    print(max_length)
            
if __name__ == "__main__":
    main()