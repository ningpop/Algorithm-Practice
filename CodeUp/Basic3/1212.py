t = list(map(int, input().split()))
t.sort()
if t[2] < t[0] + t[1]:
    print('yes')
else:
    print('no')