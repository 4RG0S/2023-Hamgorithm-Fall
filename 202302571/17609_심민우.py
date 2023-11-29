from sys import stdin
input = stdin.readline

t = int(input())
S = ""

def check(s, e, ans):
    while s < e:
        if S[s] != S[e]:
            if ans == 1:
                ans = 2
                break

            if S[s + 1] == S[e] and S[s] == S[e - 1]:
                ans = min(check(s+1, e, 1), check(s, e-1, 1))
                return ans

            elif S[s + 1] == S[e]:
                s += 1
                ans = 1

            elif S[s] == S[e - 1]:
                e -= 1
                ans = 1

            else:
                ans = 2
                break

        else:
            s += 1
            e -= 1

    return ans

for _ in range(t):
    S = str(input())
    S = S.strip()

    print(check(0,len(S)-1, 0))