# 2022.02.12
# 제한 시간 20분 / 풀이 시간 16분 40초
# 채점 결과: 정답
# 시간복잡도: O(N)

location = input()

board_size = 8
row = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

x, y = row[location[0]], int(location[1])
moving = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

count = 0
for next_loc in moving:
    nx = x + next_loc[0]
    ny = y + next_loc[1]
    if nx < 1 or ny < 1 or nx > board_size or ny > board_size:
        continue
    count += 1

print(count)