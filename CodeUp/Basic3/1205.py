a, b = map(int, input().split())
result = []
result.append(a+b)
result.append(b+a)

result.append(a-b)
result.append(b-a)

result.append(a*b)
result.append(b*a)

result.append(a/b)
result.append(b/a)

result.append(a**b)
result.append(b**a)

print(format(max(result), '.6f'))