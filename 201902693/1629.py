a, b, c = map(int,input().split())

# x ^ 4 = (x ^ 2) * (x ^ 2)
# x ^ 5 = (x ^ 2) * (x ^ 2) * x
# 곱연산을 줄여서 시간초과 해결
def mul(a, b, c) :
    if (b == 1) :
        return a % c
    elif b % 2 == 0 :
        temp = mul(a, b // 2, c)
        return (temp * temp) % c
    else :
        temp = mul(a, (b - 1) // 2, c)
        return (temp * temp * a) % c

print(mul(a, b, c))