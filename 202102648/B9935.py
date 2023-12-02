import sys
input = sys.stdin.readline

n = input().rstrip()
m = input().rstrip()

st = []
m_len = len(m)

for c in n:
    st.append(c)
    if ''.join(st[-m_len:]) == m:
        del st[-m_len:]

ans = ''.join(st)

if ans == '':
    print('FRULA')
else:
    print(ans)
