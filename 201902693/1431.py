n = int(input())
serial = []
for _ in range(n) :
    serial.append(input())

def serial_sum(s) :
    temp = 0
    for i in s :
        if i.isdigit() :
            temp += int(i)
    return temp

serial.sort(key= lambda x : (len(x), serial_sum(x), x))

for i in serial :
    print(i)