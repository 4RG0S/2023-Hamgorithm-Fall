import sys
def gcd(x,y):
    mod = x%y
    while mod > 0:
        x = y
        y = mod 
        mod = x%y
    return y
a1, b1 = map(int,sys.stdin.readline().split())
a2, b2 = map(int,sys.stdin.readline().split())
n = gcd(a1*b2 + a2 * b1,b1*b2)

son =  (a1*b2 + a2 * b1) // n
mother = b1*b2 // n

print(son,mother)