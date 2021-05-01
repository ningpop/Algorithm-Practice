month = int(input())

if 0 < month <= 2 or month == 12:
    print('winter')
elif month // 3 == 1:
    print("spring")
elif 6 <= month <= 8:
    print('summer')
elif 9 <= month <= 11:
    print('fall')