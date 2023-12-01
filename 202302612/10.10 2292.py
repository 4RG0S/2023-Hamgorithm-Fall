a = int(input())
b = 1
c = 0
while True:
    b += c*6 
    
    if b >= a:
        break
    c+=1

print(c+1)