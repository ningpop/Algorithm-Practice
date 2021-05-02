n = int(input())
a = list(map(int, input().split()))

chul = {}
for i in range(23):
    chul[i+1] = 0

for i in a:
    chul[i] += 1

for i in chul.values():
    print(i, end=' ')