from collections import deque

def main():
    n, k = map(int, input().split())
    num = input()

    # stack의 top이 현재 들어오는 값보다 작으면 pop
    st = deque([num[0]])
    for i in range(1, n):
        while k > 0 and len(st) > 0 and st[-1] < num[i]:
            st.pop()
            k -= 1
        st.append(num[i])
    
    while k > 0:
        st.pop()
        k -= 1
    print(''.join(st))
    
if __name__ == "__main__":
    main()