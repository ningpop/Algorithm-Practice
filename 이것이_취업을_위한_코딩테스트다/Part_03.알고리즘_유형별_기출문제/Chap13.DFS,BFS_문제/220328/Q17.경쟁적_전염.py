# 2022.03.29
# 제한 시간 50분 / 풀이 시간 41분 03초
# 채점 결과: 정답
# 시간복잡도: O(N^2)
# 문제 링크: https://www.acmicpc.net/problem/18405

from collections import deque

n, k = map(int, input().split())

board = [ [-1] * (n + 1) ]
for _ in range(1, n + 1):
    row = list(map(int, input().split()))
    board.append([-1] + row)

s, x, y = map(int, input().split())

initial_location = {}
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if 0 < board[i][j] <= k:
            initial_location[board[i][j]] = deque([(i, j)])
            initial_location[board[i][j]].append((-1, -1))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(s):
    for j in range(1, k + 1):
        while True:
            hx, hy = initial_location[j].popleft()
            if hx == -1 and hy == -1:
                break
            for d in range(4):
                nx = hx + dx[d]
                ny = hy + dy[d]
                if nx <= 0 or n < nx or ny <= 0 or n < ny:
                    continue
                if board[nx][ny] == 0:
                    board[nx][ny] = j
                    initial_location[j].append((nx, ny))
            initial_location[j].append((-1, -1))

if board[x][y] == 0:
    print(0)
else:
    print(board[x][y])