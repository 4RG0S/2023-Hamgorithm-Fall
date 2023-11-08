a, b = map(int, input().split())
c, d = map(int, input().split())

n = a * d + c * b
m = b * d

# 시간초과
# def gcd(a, b) :
#     for i in range(1, min(a, b) + 1) :
#         if a % i == 0 and b % i == 0 :
#             cd = i
#     return cd

# def gcd(a, b) :
#     for i in range(min(a, b), 0, -1) :
#         if a % i == 0 and b % i == 0 :
#             return i

# 유클리드 호제법 사용
def gcd(a, b) :
    while b > 0 :
        a, b = b, a%b
    return a

temp = gcd(n, m)
print(int(n / temp), int(m / temp))