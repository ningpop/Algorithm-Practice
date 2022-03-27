# 2022.03.27
# 제한 시간: 40분 / 풀이 시간 51분 01초
# 채점 결과: 오답 및 제한시간 내 미해결
# 시간복잡도: O(M * N^2)
# 문제 링크: https://www.acmicpc.net/problem/15686

from itertools import combinations

def initial_chicken_length_table(n: int):
    global chicken_list
    global chicken_length_table
    for i in range(n + 1):
        for j in range(n + 1):
            if map_info[i][j] == 2:
                chicken_list.append((i, j))
            if map_info[i][j] == 1:
                chicken_length_table[(i, j)] = 1e9


def get_chicken_length(chicken_x: int, chicken_y: int, home_x: int, home_y: int) -> int:
    return abs(chicken_x - home_x) + abs(chicken_y - home_y)

n, m = map(int, input().split())
map_info = [[0] * (n + 1)]
chicken_list = []
for i in range(n):
    row = list(map(int, input().split()))
    map_info.append([0] + row)

chicken_length_table = {}
initial_chicken_length_table(n)

if len(chicken_list) == m:
    for x, y in chicken_list:
        for key in chicken_length_table:
            value = chicken_length_table[key]
            chicken_length_table[key] = min(value, get_chicken_length(x, y, key[0], key[1]))
else:
    reduce_chicken_list = list(combinations(chicken_list, m))
    chicken_length_table = {}
    for result in reduce_chicken_list:

        for x, y in result:
            for key in chicken_length_table:
                value = chicken_length_table[key]
                chicken_length_table[key] = min(value, get_chicken_length(x, y, key[0], key[1]))

print(chicken_length_table)
result = 0
for value in chicken_length_table.values():
    result += value
print(result)