import sys


n = int(sys.stdin.readline())

def find(x):
    for i in range(2, int(x**0.5) + 1):
        if int(x) % i == 0:
            return False
    return True


def dfs(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(10):
            temp = num * 10 + i
            if find(temp):
                dfs(temp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)