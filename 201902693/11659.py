import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
sum_lst = [0] * (n + 1)
result = []
# 시간초과
# for _ in range(m) :
#     i, j = map(int, input().split())
#     result.append(sum(lst[i - 1 : j]))

# for i in range(len(result)) :
#     print(result[i])
for i in range(n) :
    sum_lst[i + 1] = sum_lst[i] + lst[i]
for _ in range(m) :
    i, j = map(int, input().split())
    print(sum_lst[j] - sum_lst[i - 1])
    