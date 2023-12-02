n, m = map(int, input().split())
arr = [i for i in range(n, m+1)]
alphaArr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
dic = {}

for i in range(len(arr)):
    if arr[i] < 10:
        dic[alphaArr[arr[i]]] = arr[i]
    else:
        dic[(alphaArr[arr[i]//10] + ' ' + alphaArr[arr[i]%10])] = arr[i]

dic = sorted(dic.items(), key=lambda x: x[0])

for i in range(len(dic)):
    print(dic[i][1], end=' ')
    if (i+1) % 10 == 0:
        print()