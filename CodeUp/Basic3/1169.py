y = int(input())
birth = str(2012 - y + 1)
if birth[:2] == '19':
    print(int(birth[2:]), 1)
else:
    print(int(birth[2:]), 3)