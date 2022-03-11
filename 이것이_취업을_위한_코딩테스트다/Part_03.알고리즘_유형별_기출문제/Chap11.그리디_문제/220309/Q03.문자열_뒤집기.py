# 2022.03.11
# 제한 시간 20분 / 풀이 시간 17분 03초
# 채점 결과: 정답
# 시간복잡도: O(N)

s = input()

zero_string = ''
one_string = ''

for i in range(len(s)):
    if s[i] == '0':
        if i == 0:
            pass
        elif s[i - 1] == '1':
            zero_string += ' '
        zero_string += '0'
    else:
        if i == 0:
            pass
        elif s[i - 1] == '0':
            one_string += ' '
        one_string += '1'

zero_count = len(zero_string.split())
one_count = len(one_string.split())

print(min(zero_count, one_count))