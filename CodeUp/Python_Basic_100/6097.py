h, w = map(int, input().split())
n = int(input())
pan = [ [0] * w for _ in range(h) ]

for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(y, y+l):
            pan[x-1][j-1] = 1
    else:
        for j in range(x, x+l):
            pan[j-1][y-1] = 1

for i in pan:
    for j in i:
        print(j, end=' ')
    print()