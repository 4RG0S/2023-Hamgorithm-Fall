g,l = map(int, input().split())
div = l // g
a,b = 1, div

def gcd(a,b):
    while b:
        mod = b
        b = a%b
        a = mod
    return a


for i in range(1, div//2+1):
    if div % i ==0:
        c = i
        d = div//i
        if gcd(c,d) != 1:
            continue
        if a+b > c+d:
            a = c
            b=  d
print(a*g, b*g)