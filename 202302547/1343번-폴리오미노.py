str = list(input().split('.'))
strResult = ''
a = 0
b = 0

for i in range (len(str)):
    if len(str[i]) % 2 != 0:
        print(-1)
        exit()
    else:
        a = len(str[i]) // 4
        b = (len(str[i]) - 4 * a) // 2
        if len(str[i]) >= 4:
            strResult += 'AAAA' * a
            strResult += 'BB' * b
            # strResult = 'AAAA' * 2 + 'BB' * 1
        else:
            strResult += 'BB' * b
        strResult += '.'
    
print(strResult[:-1])