n = int(input())

s, c = 0, 0
while True :
    s += c
    c += 1
    if s>=n :
        break

print(s)