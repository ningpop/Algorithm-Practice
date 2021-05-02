sound = list(map(int, input().split()))

result = 1
for i in sound:
    result *= i

print(format(result / (8 * 1024 * 1024), '.1f'), 'MB')