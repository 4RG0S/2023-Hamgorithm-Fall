a = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,
'August':8,'September':9,'October':10,'November':11,'December':12}
month, day, year, time = input().split()
month = a[month]
day = int(day[:-1])
h = int(time[0:2])
m = int(time[3:])
year = int(year)

a=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    a[1] += 1

time = sum(a) * 24 * 60
b = (sum(a[:month-1]) + day - 1) * 24 * 60 + h * 60 + m
print(b / time * 100)

# import datetime as dt

# str = list(input().split(' '))

# month = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# str_y = int(str[2])
# str_m = int(month.index(str[0]))
# str_d = int(str[1][:-1]) 
# str_h = int(str[3][:-3])
# str_min = int(str[3][3:5])

# date1 = dt.datetime(str_y, 12, 31, 23, 59, 59)
# date2 = dt.datetime(str_y, str_m, str_d, str_h, str_min, 0)
# date3 = (date1 - date2).total_seconds()

# # print(date1)
# # print(date2)
# # print(date3)
# # print((60 * 60 * 24 * 365))

# if date2 == date1:
#     print('0.0')
# elif str_y // 400 == 0 or (str_y // 4 == 0 and str_y // 100 != 0):
#     print((1 - date3 / (60 * 60 * 24 * 365.2425)) * 100)
# else:
#     print((1 - date3 / (60 * 60 * 24 * 365)) * 100)