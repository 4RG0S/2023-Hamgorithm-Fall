# 각 단어의 문자를 하나씩 배열에 저장하고,
# 그 배열에 있는 문자가 이미 나왔던 문자라면 그룹 단어가 아니게 된다.

n = int(input())
arr = [''] * n

cnt = n

for i in range(n):
    arr[i] = list(input())

for i in range(n):
    already = [''] * 100
    for j in range(len(arr[i])):
        if arr[i][j] in already:
            if arr[i][j] != arr[i][j-1]:
                cnt -= 1
                break
        else:
            already.append(arr[i][j])

print(cnt)