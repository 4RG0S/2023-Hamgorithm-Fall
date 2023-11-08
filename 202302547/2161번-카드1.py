n = int(input())
arr = [i for i in range(1, n+1)]
flag = 1

try:    
    while(True):
        if flag == 1:
            temp = arr.pop(0)
            print(temp, end=' ')
            flag = 0
        else:
            temp = arr.pop(0)
            arr.append(temp)
            flag = 1
except:
    pass