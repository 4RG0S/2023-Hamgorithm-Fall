import bisect
t = int(input())
for _ in range(t) :
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0
    A.sort()
    B.sort()
    for i in A :
        temp = bisect.bisect(B, i - 1)
        count += temp
    # 단순 비교는 시간초과
    # for i in A :
    #     for j in B :
    #         if i > j :
    #             count += 1
    print(count)