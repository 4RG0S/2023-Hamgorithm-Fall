def preorder(node):
    if node =='.':
        return
    
    print(node, end='')
    preorder(graph[node][0])
    preorder(graph[node][1])

def inorder(node):
    if node =='.':
        return
    
    inorder(graph[node][0])
    print(node, end='')
    inorder(graph[node][1])

def postorder(node):
    if node =='.':
        return
    
    postorder(graph[node][0])
    postorder(graph[node][1])
    print(node, end='')


n = int(input())

graph={}
for _ in range(n):
    root, left, right = list(input().split())
    graph[root] = [left, right]



preorder('A')
print()
inorder('A')
print()
postorder('A')
