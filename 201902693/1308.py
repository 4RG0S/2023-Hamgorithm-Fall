import datetime as dt
today = tuple(map(int, input().split()))
dday = tuple(map(int, input().split()))
if today[0] + 1000 < dday[0]:
    print('gg')
elif today[0] + 1000 == dday[0] and (today[1], today[2]) <= (dday[1], dday[2]):
    print('gg')
else:
    today = dt.date(*today)
    dday = dt.date(*dday)
    print(f'D-{dday.toordinal() - today.toordinal()}')