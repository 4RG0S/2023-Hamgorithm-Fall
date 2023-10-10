# 시간 초과
# def fib(n) :
#     global cnt0
#     global cnt1
#     if n ==0 :
#         cnt0 += 1
#         return 0
#     elif n == 1:
#         cnt1 += 1
#         return 1
#     else :
#         return fib(n - 1) + fib(n - 2)

# t = int(input())
# for _ in range(t) :
#     n = int(input())
#     cnt0 = 0
#     cnt1 = 0
#     fib(n)
#     print(cnt0, cnt1)
    
t = int(input())
for _ in range(t):
    n = int(input())
    zero, one = 1, 0
    for i in range(n):
        zero, one = one , zero + one
    print(zero, one)