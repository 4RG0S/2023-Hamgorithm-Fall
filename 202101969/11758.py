import sys
ar = []
re = True
for i in range(3):
    a,b = map(int, sys.stdin.readline().split())
    ar.append([a, b])
# print(ar)
if ((ar[0][0]*ar[1][1]+ ar[1][0]*ar[2][1] +ar[2][0]*ar[0][1] )-(ar[1][0]*ar[0][1] + ar[2][0]*ar[1][1] + ar[0][0]*ar[2][1]) >0):
    print(1)
elif((ar[0][0]*ar[1][1]+ ar[1][0]*ar[2][1] +ar[2][0]*ar[0][1] )-(ar[1][0]*ar[0][1] + ar[2][0]*ar[1][1] + ar[0][0]*ar[2][1]) <0):
    print(-1)
else:
    print(0)