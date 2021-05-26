# 2021.05.26
# 풀이시간 40분 / 제한시간 30분
# 정답 / 수행시간 초과 / 제한시간 초과
# https://www.acmicpc.net/problem/14888

from itertools import permutations

N = int(input())
n_list = list(map(int, input().split()))
op_list = list(map(int, input().split()))

operators = []
for i in range(len(op_list)):
    while op_list[i] > 0:
        if i == 0:
            operators.append('+')
        elif i == 1:
            operators.append('-')
        elif i == 2:
            operators.append('*')
        elif i == 3:
            operators.append('/')
        op_list[i] -= 1

op_list = list(permutations(operators))

max_answer = -1000000000
min_answer = 1000000000
for operate in op_list:
    answer = n_list[0]
    for i in range(len(n_list) - 1):
        if operate[i] == '+':
            answer += n_list[i + 1]
        elif operate[i] == '-':
            answer -= n_list[i + 1]
        elif operate[i] == '*':
            answer *= n_list[i + 1]
        elif operate[i] == '/':
            if answer < 0:
                answer = -answer
                answer //= n_list[i + 1]
                answer = -answer
            else:
                answer //= n_list[i + 1]
    max_answer = max(max_answer, answer)
    min_answer = min(min_answer, answer)

print(max_answer)
print(min_answer)