b, c, d = map(int, input().split())

bArr = sorted(list(map(int, input().split())), reverse=True)
cArr = sorted(list(map(int, input().split())), reverse=True)
dArr = sorted(list(map(int, input().split())), reverse=True)

min = min(len(bArr), len(cArr), len(dArr))

# print(bArr)
# print(cArr)
# print(dArr)
print(sum(bArr) + sum(cArr) + sum(dArr))
# print(min)

for i in range(min):
    bArr[i] = int(bArr[i] * 0.9)      
    cArr[i] = int(cArr[i] * 0.9)
    dArr[i] = int(dArr[i] * 0.9)

# print(bArr)
# print(cArr)
# print(dArr)
print(sum(bArr) + sum(cArr) + sum(dArr))