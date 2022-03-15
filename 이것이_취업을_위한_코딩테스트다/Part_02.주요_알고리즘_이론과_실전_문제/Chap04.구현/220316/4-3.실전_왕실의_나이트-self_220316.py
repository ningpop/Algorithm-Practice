# 2022.03.16
# 제한 시간 20분 / 풀이 시간 16분 25초
# 채점 결과: 정답
# 시간복잡도: O(N)

location = input()

col = ord(location[0]) - 96
row = int(location[1])

direction = [
    (2, -1), (2, 1), (1, 2), (-1, 2),
    (-2, 1), (-2, -1), (-1, -2), (1, -2)
]

count = 0
for i, j in direction:
    ncol = col - i
    nrow = row - j
    if ncol <= 0 or 8 < ncol or nrow <= 0 or 8 < nrow:
        continue
    count += 1

print(count)