image = list(map(int, input().split()))

result = 1
for i in image:
    result *= i

print(format(result / (8*1024*1024), '.2f'), 'MB')