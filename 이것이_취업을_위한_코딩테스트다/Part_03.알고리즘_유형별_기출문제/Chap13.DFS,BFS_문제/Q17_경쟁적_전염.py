# 2021.05.23
# 풀이시간 60분 / 제한시간 50분
# 정답 / 제한시간 초과
# https://www.acmicpc.net/problem/18405

from collections import deque

N, K = map(int, input().split())

plate = []
for _ in range(N):
    plate.append(list(map(int, input().split())))

S, X, Y = map(int, input().split())

virus = deque()
for v in range(1, K+1):
    for idx, row in enumerate(plate):
        if v in row:
            virus.append((v, idx, row.index(v)))
virus.append((0, 0, 0))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

S -= 1
while S >= 0:
    # print(virus)
    v, i, j = virus.popleft()
    if v == 0:
        S -= 1
        continue
    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if plate[nx][ny] == 0:
                plate[nx][ny] = v
                virus.append((v, nx, ny))
    virus.append((0, 0, 0))

print(plate[X-1][Y-1])