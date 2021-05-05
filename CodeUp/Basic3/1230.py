t = list(map(int, input().split()))

if min(t) > 170:
    print('PASS')
else:
    for i in t:
        if i <= 170:
            print('CRASH', i)
            break