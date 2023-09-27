import sys
input = sys.stdin.readline

s = input().strip()

st = set()

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        st.add(s[i:j])

print(len(st))
