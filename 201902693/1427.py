n = list(input())

n.sort(reverse=True)
result = ''
for i in n :
    result += i

print(result)