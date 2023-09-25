import sys
input = sys.stdin.readline
m = int(input())
s = set()
for _ in range(m) :
    lst = list(input().split())
    a = lst[0]
    if a == 'add' :
        s.add(int(lst[1]))
        # print(s)
    elif a == 'remove' :
        if int(lst[1]) in s :
            s.remove(int(lst[1]))
            # print(s)
    elif a == 'check' :
        if int(lst[1]) in s :
            print(1)
            # print(s)
        else :
            print(0)
            # print(s)
    elif a == 'toggle' :
        if int(lst[1]) in s :
            s.remove(int(lst[1]))
            # print(s)
        else :
            s.add(int(lst[1]))
            # print(s)
    elif a == 'all' :
        s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
        # print(s)
    elif a == 'empty' :
        s = set()
        # print(s)