# 2021.05.30
# 풀이시간 20분 / 제한시간 20분
# 수행시간 초과
# https://www.acmicpc.net/problem/18310

# import time
# start = time.time()
# n = 4
# house_list = [5, 1, 7, 9]

import sys

n = int(sys.stdin.readline())
house_list = list(map(int, sys.stdin.readline().split()))

result = (1e5, 0)
for i in house_list: # 안테나 설치 집
    sum = 0
    for j in house_list: # 다른 집 순회
        if i == j:
            continue
        sum += abs(i - j)
    if result[0] > sum:
        result = (sum, i)

print(result[1])
# print(time.time() - start)