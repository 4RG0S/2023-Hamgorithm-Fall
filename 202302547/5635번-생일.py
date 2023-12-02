n = int(input())
arr = []

large_year = 9999
large_month = 9999
large_day = 9999
large_name =''

small_year = 0
small_month = 0
small_day = 0
small_name =''

for i in range(n):
    arr.append(list(input().split()))
    
    if small_year < int(arr[i][3]):
        small_year = int(arr[i][3])
        small_month = int(arr[i][2])
        small_day = int(arr[i][1])
        small_name = arr[i][0]
    elif small_year == int(arr[i][3]):
        if small_month < int(arr[i][2]):
            small_year = int(arr[i][3])
            small_month = int(arr[i][2])
            small_day = int(arr[i][1])
            small_name = arr[i][0]
        elif small_month == int(arr[i][2]):
            if small_day < int(arr[i][1]):
                small_year = int(arr[i][3])
                small_month = int(arr[i][2])
                small_day = int(arr[i][1])
                small_name = arr[i][0]
    
    if large_year > int(arr[i][3]):
        large_year = int(arr[i][3])
        large_month = int(arr[i][2])
        large_day = int(arr[i][1])
        large_name = arr[i][0]
    elif large_year == int(arr[i][3]):
        if large_month > int(arr[i][2]):
            large_year = int(arr[i][3])
            large_month = int(arr[i][2])
            large_day = int(arr[i][1])
            large_name = arr[i][0]
        elif large_month == int(arr[i][2]):
            if large_day > int(arr[i][1]):
                large_year = int(arr[i][3])
                large_month = int(arr[i][2])
                large_day = int(arr[i][1])
                large_name = arr[i][0]
            
print(small_name)
print(large_name)