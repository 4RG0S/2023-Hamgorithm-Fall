import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dic = {}
result = []

for _ in range(n) :
    site, pswd = input().split()
    dic[site] = pswd

for _ in range(m) :
    target = input().strip()
    result.append(dic.get(target))
print('\n'.join(result))
