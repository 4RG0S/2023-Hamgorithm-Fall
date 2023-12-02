import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
tree = []

while True:
    try:
        tree.append(int(input()))
    except:
        break

def recursion(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if tree[i] > tree[start]:
            mid = i
            recursion(start + 1, i - 1)
            recursion(i, end)
            print(tree[start])
            return
        
    recursion(start + 1, end)
    print(tree[start])
    return

recursion(0, len(tree) - 1)
