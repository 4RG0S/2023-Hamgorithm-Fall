import sys
n = int(input())
nums = list(map(int, input().split()))
result = sys.maxsize
nums.sort()
three = [0,0,0]

def two_pointer(start, end, fix):
    global result
    if result == 0:
        return
    while start < end:
        s = nums[start] + nums[end] + nums[fix]
        if abs(s) < result:
            result = abs(s)
            three[0] = nums[fix]
            three[1] = nums[start]
            three[2] = nums[end]

            if result == 0:
                return

        if s < 0:
            start += 1
        elif s > 0:
            end -= 1

for i in range(0,n-2):
    two_pointer(i+1, n-1, i)


print(*three)