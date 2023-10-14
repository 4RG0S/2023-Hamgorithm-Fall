def myfunc(index, len):
    if len <= 1:
        return
    
    n = len // 3
    for i in range(index + n, index + n*2): 
        this_line[i] = ' '

    myfunc(index, n) 

    myfunc(index + n * 2, n) 

while True:
    try:
        n = int(input())
        this_line = ['-'] * (3 ** n)
        myfunc(0, 3 ** n)
        print(''.join(this_line))
    except:
        break