n = int(input())
p = list(map(int, input().split()))
p.sort()
sum_lst = [0] * (n + 1)

for i in range(n) :
    sum_lst[i + 1] = sum_lst[i] + p[i]

print(sum(sum_lst))