ydm, g = input().split()
if 1 <= int(g) <=2:
    print(2012 - int('19' + ydm[:2]) + 1)
else:
    print(2012 - int('20' + ydm[:2]) + 1)