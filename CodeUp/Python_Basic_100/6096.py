d = []
for i in range(1, 20):
    row = list(map(int, input().split()))
    d.append(row)

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(1, 20):
        if d[j-1][y-1] == 0:
            d[j-1][y-1] = 1
        else:
            d[j-1][y-1] = 0

        if d[x-1][j-1] == 0:
            d[x-1][j-1] = 1
        else:
            d[x-1][j-1] = 0

for i in d:
    for j in i:
        print(j, end=' ')
    print()