m, n = map(int, input().split())
lst = []
dic = {'0' : 'zero', '1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four', '5' : 'five', '6': 'six', '7': 'seven', '8' : 'eight', '9' : 'nine'}

for i in range(m, n + 1) :
    temp = ' '
    for j in str(i) :
        temp += dic[j] + ' '
    temp = temp.strip()
    lst.append([i, temp])

lst.sort(key= lambda x: x[1])

for i in range(len(lst)) :
    if i % 10 == 0 and i // 10 != 0 :
        print(sep='\n')
    print(lst[i][0], end = ' ')