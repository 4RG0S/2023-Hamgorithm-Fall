num = list(input())
cheak = [0] * 10
max = 1

for i in range(len(num)):
    if num[i] == '9':
        num[i] = '6'
    
    temp = int(num[i])
    cheak[temp] += 1

for i in range(10):
    if max < cheak[i] and i != 6:
        max = cheak[i]

six = cheak[6] // 2 + cheak[6] % 2

if six < max:
    print(max)
else:
    print(six)

# 테스트 케이스
# 6으로만 이루어진 수
# 짝수 개
#     2 이상
#     2 이하
# 홀수 개
#     2 이상
#     2 이하
    
# 6과 다른 숫자가 섞인 수
# 짝수 개
# 홀수 개

# 다른 숫자만 있는 수
