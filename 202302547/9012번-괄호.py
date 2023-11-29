n = int(input())
for i in range(n):
    str = input()
    flag = []
    strArr = list(str)
    try:
        for i in range(len(strArr)):
            if strArr[i] == '(':
                flag.append('(')
            elif strArr[i] == '[':
                flag.append('[')
            elif strArr[i] == ')' or strArr[i] == ']':
                if flag[-1] == '(' and strArr[i] == ')':
                    flag.pop()
                elif flag[-1] == '[' and strArr[i] == ']':
                    flag.pop()
                else:
                    break
            else:
                continue
        if len(flag) == 0:
            print('YES')
        else:
            print('NO')
    except:
        print('NO')        