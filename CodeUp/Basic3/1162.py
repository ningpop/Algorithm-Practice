y, m, d = map(int, input().split())
if (y-m+d)%10 == 0:
    print('대박')
else:
    print('그럭저럭')