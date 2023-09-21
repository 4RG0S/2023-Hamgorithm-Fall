import sys
a,b = map(int,sys.stdin.readline().split())
count = 1
while(a!=b):
    count += 1
    tmp = b
    if b%10 ==1:
        b//= 10
    elif b%2 ==0:
        b//=2
    
    if tmp == b:
        print(-1)
        break
else:
    print(count)