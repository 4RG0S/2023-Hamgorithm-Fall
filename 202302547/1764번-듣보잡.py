import sys

input = sys.stdin.readline
n, m = map(int, input().split())

hear = set()
see = set()

for _ in range(n):
    hear.add(input())
    
for _ in range(m):
    see.add(input())

common_words = sorted(hear.intersection(see))

print(len(common_words))
for word in common_words:
    print(word, end="")
