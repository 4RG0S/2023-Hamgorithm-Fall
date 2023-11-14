n = input()
result = 0

for i in range(1, len(n)) :
    result += 9 * 10**(i - 1) * i
result += ((int(n) - 10 ** (len(n) - 1)) + 1) * len(n)

print(result)