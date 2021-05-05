t, a, b = map(int, input().split())
m = 90 - t
if m%5 == 0:
    if (a + m//5) > b:
        print('win')
    elif (a + m//5) < b:
        print('lose')
    else:
        print('same')
else:
    if (a + m//5 + 1) > b:
        print('win')
    elif (a + m//5 + 1) < b:
        print('lose')
    else:
        print('same')