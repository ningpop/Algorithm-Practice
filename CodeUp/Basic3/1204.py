n = int(input())
if n%10 == 1:
    if n == 11:
        print(str(n)+'th')
    else:
        print(str(n)+'st')
elif n%10 == 2:
    if n == 12:
        print(str(n)+'th')
    else:
        print(str(n)+'nd')
elif n%10 == 3:
    if n == 13:
        print(str(n)+'th')
    else:
        print(str(n)+'rd')
else:
    print(str(n)+'th')