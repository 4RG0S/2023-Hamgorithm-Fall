# 5로 나누어 떨어질 수 있는지 확인
# 3으로 나누어 떨어질 수 있는지 확인
# 5와 3로 나누어 떨어질 수 있는지 확인

n = int(input())

if n % 5 == 0:
    print(n//5)
elif n % 3 == 0 and n // 5 < 0:
    print(n//3)
else:
    div = n//5
    rm = n % 5
    while div >= 0:
        if rm % 3 == 0:
            print(div + rm//3)
            break
        else:
            div -= 1
            rm += 5
    if div < 0:
        print(-1)