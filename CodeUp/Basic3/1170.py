a, b, c = map(int, input().split())
if c//10 >= 1:
    print(str(a)+str(b)+str(c))
else:
    print(str(a)+str(b)+'0'+str(c))