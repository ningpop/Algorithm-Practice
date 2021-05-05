yut = list(map(int, input().split()))
result = yut.count(1)
if result == 1:
    print('도')
elif result == 2:
    print('개')
elif result == 3:
    print('걸')
elif result == 4:
    print('윷')
else:
    print('모')