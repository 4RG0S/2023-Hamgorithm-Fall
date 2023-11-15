a = int(input())
b = input()
res = 0

for i in range(len(b)-1, 0, -1):
    print(int(b[i]) * a)

print(a * int(b))