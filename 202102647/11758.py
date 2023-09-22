import sys
dots = []
for _ in range (3):
    dots.append(list(map(int,sys.stdin.readline().split())))

p1 = dots[0]
p2 = dots[1]
p3 = dots[2]
# 신발끈 공식
answer1 = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]
answer2 = p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1]

answer = answer1-answer2

#반시계
if answer > 0 :
    print(1)
elif answer == 0:
    print(0)
else:
    print(-1)