import sys
input = sys.stdin.readline

n = int(input())
dp_max = [0, 0, 0]
dp_min = [0, 0, 0]

for _ in range(n):
    m = list(map(int, input().split()))
    
    dp = []
    dp.append(m[0] + max(dp_max[0], dp_max[1]))
    dp.append(m[1] + max(dp_max))
    dp.append(m[2] + max(dp_max[1], dp_max[2]))
    dp_max = dp
    
    dp = []
    dp.append(m[0] + min(dp_min[0], dp_min[1]))
    dp.append(m[1] + min(dp_min))
    dp.append(m[2] + min(dp_min[1], dp_min[2]))
    dp_min = dp
    
print(max(dp_max), min(dp_min))