s = input()

for i in range(len(s)) :
    # 문자열 앞에서부터 탐색하면서 자른 문자열이 팰린드롬이라면
    # 자르기 전 문자열 수만큼 붙여주면 된다.
    if s[i:] == s[i:][::-1] :
        print(len(s) + i)
        break