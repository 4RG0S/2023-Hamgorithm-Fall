# n, d = map(int,input().split())
# s = ""
# for i in range(1, n + 1) :
#     s += str(i)
# print(s.count(str(d)))

n, d = input().split()
temp = int(n)
s = ""
for i in range(1, temp + 1) :
    s += str(i)
print(s.count(d))