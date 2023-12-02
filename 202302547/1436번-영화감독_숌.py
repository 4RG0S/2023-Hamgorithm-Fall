import sys

input = sys.stdin.readline
n = int(input())

result = []

for i in range(666, 10000000):
    if '666' in str(i):
        result.append(i)
        
print(result[n-1])
print(len(result))