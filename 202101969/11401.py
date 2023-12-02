import sys

def read_input():
    return map(int, sys.stdin.readline().split())

def calculate_power(a, b, p):
    if b == 0:
        return 1
    if b % 2:
        return (calculate_power(a, b//2, p) ** 2 * a) % p
    else:
        return (calculate_power(a, b//2, p) ** 2) % p

def main():
    p = 1000000007
    N, K = read_input()

    factorial = [1] * (N+1)

    for i in range(2, N+1):
        factorial[i] = (factorial[i-1] * i) % p

    A = factorial[N]
    B = (factorial[N-K] * factorial[K]) % p
    result = (A % p) * (calculate_power(B, p-2, p) % p) % p
    print(result)

if __name__ == "__main__":
    main()
