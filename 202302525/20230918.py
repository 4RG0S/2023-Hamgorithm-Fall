for _ in range(int(input())):
    h, w, n = map(int, input().split())
    t = n % h
    b = n // h + 1
    if t == 0:
        t = h
        b -= 1
    print(f'{t * 100 + b}')