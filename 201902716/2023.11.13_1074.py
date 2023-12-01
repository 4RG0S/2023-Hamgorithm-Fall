import sys

def z_order(N, r, c):
    if N == 1:
        return 2*r + c
    else:
        half = 2**(N-1)
        if r < half and c < half:
            return z_order(N-1, r, c)
        elif r < half and c >= half:
            return half**2 + z_order(N-1, r, c-half)
        elif r >= half and c < half:
            return 2*half**2 + z_order(N-1, r-half, c)
        else:
            return 3*half**2 + z_order(N-1, r-half, c-half)

def main():
    N, r, c = map(int, sys.stdin.readline().rstrip().split())
    print(z_order(N, r, c))
        
if __name__ == "__main__":
    main()
