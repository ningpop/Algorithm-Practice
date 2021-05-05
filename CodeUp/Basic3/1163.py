y, m, d = map(int, input().split())
if int(str(y+d+m)[-3])%2 == 0:
    print('대박')
else:
    print('그럭저럭')