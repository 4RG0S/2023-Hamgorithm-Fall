def dac(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (dac(a,b//2,c)**2)%c
    else:
        return ((dac(a,b//2,c)**2)*a)%c

abc = list(map(int, input().split()))
print(dac(abc[0], abc[1], abc[2]))