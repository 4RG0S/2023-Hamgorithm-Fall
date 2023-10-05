while True:
    total = int(input())
    if total == 0:
        break
    else:
        page = []
        arr = list(input().split(','))

        for  i in range(len(arr)):
            if '-' in arr[i]:
                arr[i] = arr[i].split('-')
                arr[i] = list(map(int, arr[i]))
                arr[i] = list(range(arr[i][0], arr[i][1]+1))
            else:
                arr[i] = int(arr[i])
                if arr[i] < total+1 and arr[i] < 1001:
                    page.append(arr[i])
        
        for i in range(len(arr)):
            if type(arr[i]) == list:
                for j in range(len(arr[i])):
                    if arr[i][j] < total+1 and arr[i][j] < 1001:
                        page.append(arr[i][j])
                    else:
                        break
            else:
                continue
                
        page = list(set(page))

        print(len(page))