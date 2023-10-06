d,k = map(int,input().split())
a = 1
b = 1
for _ in range (d-3):
    a,b = b, a+b
save = 0
first = 1
second = 0
while True:
    temp = k-a*first
    if temp < 0:
        break
    if temp % b == 0:
        second = temp // b
        break
    first+= 1
        
print(first)
print(second)