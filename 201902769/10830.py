import sys

def multiply(A, B, N):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 1000
    return result

def power(A, B, N):
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A
    elif B % 2 == 0:
        temp = power(A, B // 2, N)
        return multiply(temp, temp, N)
    else:
        return multiply(A, power(A, B - 1, N), N)

N, B = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = power(A, B, N)
for row in result:
    print(*row)
