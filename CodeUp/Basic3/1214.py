day = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
y, m = map(int, input().split())
if m == 2:
    if ((y%4 == 0) and (y%100 != 0)) or y%400 == 0:
        print(29)
    else:
        print(28)
else:
    print(day[m])