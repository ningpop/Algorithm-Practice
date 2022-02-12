# 2022.02.12
# 제한 시간 40분 / 풀이 시간 43분 34초
# 채점 결과: 정답
# 시간복잡도: N + N^2 = O(N^2)

row, column = map(int, input().split())
x, y, d = map(int, input().split())
board = []
have_gone = []
for i in range(row):
    board.append(list(map(int, input().split())))
    have_gone.append([0, 0, 0, 0])

direction = [(0, -1), (-1, 0), (0, 1), (1, 0)] # N W S E

have_gone[y][x] = 1
while True:
    d += 1 # 매뉴얼 1번: 갈 곳 정하기
    if d > 3:
        d = 0
    nx = x + direction[d][0]
    ny = y + direction[d][1]
    if have_gone[ny][nx] == 0 and board[ny][nx] == 0:
        x, y = nx, ny
        have_gone[y][x] = 1
    else:
        nx = x - direction[d][0]
        ny = y - direction[d][1]
        if board[ny][nx] == 1:
            break
        x, y = nx, ny
        have_gone[y][x] = 1

count = 0
for i in range(row):
    for j in range(column):
        if have_gone[i][j] == 1:
            count += 1

print(count)
