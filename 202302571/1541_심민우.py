import sys
input = sys.stdin.readline

s = input()
ssm = s.split('-')
lsum = []
for ts in ssm:
    lsum.append(sum(map(int,ts.split('+'))))

ans = lsum[0]
for i in range(1,len(lsum)):
    ans -= lsum[i]

print(ans)