str = input()
word = input()
count = 0

point = 0
for i in range(len(str)+1):
    # print(point, i)
    # print(str[point:i])
    if word in str[point:i]:
        count += 1
        point = i
    else:
        continue
    
print(count)