a_len, b_len = map(int, input().split())

a_arr = set(map(int, input().split()))
b_arr = set(map(int, input().split()))

temp1 = a_arr - b_arr
temp2 = b_arr - a_arr

print(len(temp1)+len(temp2))