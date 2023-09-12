Number, Hab = map(int, input().split())
a = list(map(int, input().split()))
s = 0
reco = [0] * Hab

for i in range(Number):
    s += a[i]
    reco[s%Hab] +=1

result = reco[0]

for i in reco:
    result += i *(i-1)//2

print(result)