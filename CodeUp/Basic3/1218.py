a, b, c = map(int, input().split())
if (a+b) <= c:
    print('삼각형아님')
elif a==b==c:
    print('정삼각형')
elif a==b or b==c or a==c:
    print('이등변삼각형')
elif pow(a, 2) + pow(b, 2) == pow(c, 2):
    print('직각삼각형')
else:
    print('삼각형')