# 2022.04.03
# 제한 시간 30분 / 풀이 시간 23분 46초
# 채점 결과: 오답(시간초과)
# 시간복잡도: O(N!)
# 문제 링크: https://www.acmicpc.net/problem/14888

from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
operator_list = list(map(int, input().split()))
operators = []
for idx, val in enumerate(operator_list):
    if val > 0:
        for i in range(val):
            operators.append(idx)

operators_cases = list(permutations(operators, n - 1))

max_result = -1e9
min_result = 1e9
for case in operators_cases:
    result = numbers[0]
    for i in range(1, n):
        op = case[i - 1]
        num = numbers[i]

        if op == 0: # +
            result += num
        elif op == 1: # -
            result -= num
        elif op == 2: # *
            result *= num
        elif op == 3: # /
            if result < 0:
                result = -((-result) // num)
            else:
                result //= num

    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)