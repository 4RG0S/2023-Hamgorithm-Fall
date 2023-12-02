na, nb = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

result = a - b

if len(result) == 0 :
    print(0)
else :
    print(len(result))
    print(*sorted(list(result)))