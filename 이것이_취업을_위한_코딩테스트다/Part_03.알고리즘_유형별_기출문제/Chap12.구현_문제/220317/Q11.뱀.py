# 2022.03.23
# 제한 시간: 40분 / 풀이 시간 40분 00초
# 채점 결과: 오답 및 제한시간 내 미해결
# 시간복잡도: 
# 문제 링크: https://www.acmicpc.net/problem/3190

def change_direction():
    global direction
    if direction >= 3:
        direction = 0
    direction += 1

n = int(input())
k = int(input())
apples = []
for _ in range(k):
    apples.append(tuple(map(int, input().split())))
l = int(input())
move = []
for _ in range(l):
    sec, direction = input().split()
    move.append((int(sec), direction))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

map_info = [ [0] * n for _ in range(n) ]
for i, j in apples:
    map_info[i - 1][j - 1] = 1

x = y = tx = ty = 1
direction = 0
time = 0
while True:
    time += 1

    hx = x + dx[direction]
    hy = y + dy[direction]

    if map_info[hx - 1][hy - 1] == 1:
        pass
    else:
        map_info[hx - 1][hy - 1] = 2
        tx = hx
        ty = hy