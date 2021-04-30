import sys

S = sys.stdin.readline()

eng = [ i for i in S if i.isalpha()]
num = [ int(i) for i in S if i.isdigit()]

result = ''
for i in sorted(eng):
    result += i

result += str(sum(num))
print(result)