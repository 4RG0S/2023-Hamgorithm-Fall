def main():
    n = int(input())
    light = input()
    rgb = {'R':'G', 'G':'B', 'B':'R'}
    
    ans = 1000000
    for color in ['R', 'G', 'B']:
        cnt = 0
        copy = list(light)
        for i in range(n-2):
            for _ in range(2):
                if copy[i] != color:
                    copy[i] = rgb[copy[i]]
                    copy[i+1] = rgb[copy[i+1]]
                    copy[i+2] = rgb[copy[i+2]]
                    cnt += 1
        if copy[-1] == color and copy[-2] == color:
            ans = min(ans, cnt)
    
    if ans == 1000000:
        ans = -1
    print(ans)
    
if __name__ ==  "__main__":
    main()