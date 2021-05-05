a, b = map(int, input().split())
m = 90 - a
if m%5 == 0:
    print(m//5 + b)
else:
    print(m//5 + 1 + b)