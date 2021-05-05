a, b = map(int, input().split())
if b%a == 0:
    print(str(a)+'*'+str(b//a)+'='+str(b))
elif a%b == 0:
    print(str(b)+'*'+str(a//b)+'='+str(a))
else:
    print('none')