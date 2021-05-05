n = input()
z = int(n[1]+n[0])*2
if z >= 100:
    z = int(str(z)[1:])
print(z)
if z <= 50:
    print('GOOD')
else:
    print('OH MY GOD')