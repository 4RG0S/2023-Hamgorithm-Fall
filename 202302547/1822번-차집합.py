a_len, b_len = map(int, input().split())

a_arr = set(map(int, input().split()))
b_arr = set(map(int, input().split()))

temp1 = a_arr - b_arr

if len(temp1) == 0:
    print(0)
else:
    temp1 = sorted(temp1)
    print(len(temp1))
    print(*temp1)