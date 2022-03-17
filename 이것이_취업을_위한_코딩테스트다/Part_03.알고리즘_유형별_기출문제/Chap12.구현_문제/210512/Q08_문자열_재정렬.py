import sys

S = sys.stdin.readline()

eng = [ i for i in S if i.isalpha()]
num = [ int(i) for i in S if i.isdigit()]

result = ''
for i in sorted(eng):
    result += i

result += str(sum(num))
print(result)

# input: 'K1KA5CB7'
# >>> 0.00010910000000000086sec

# input: 'AJKDLSI412K4JSJ9D'
# >>> 0.00010139999999999802sec