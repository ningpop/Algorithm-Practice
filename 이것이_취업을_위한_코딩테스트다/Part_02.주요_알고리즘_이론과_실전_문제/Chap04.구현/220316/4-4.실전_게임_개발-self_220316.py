# 2022.03.16
# 제한 시간 40분 / 풀이 시간 40분 00초
# 채점 결과: 오답 및 제한시간 내 미해결
# 시간복잡도: 개판

n, m = map(int, input().split())
a, b, d = map(int, input().split())
board = []
is_visited = []
for _ in range(n):
    board.append(list(map(int, input().split())))
    is_visited.append([ 0 for _ in range(m) ])

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def change_direction():
    global d
    d -= 1
    if d < 0:
        d = 3

is_visited[a][b] = 1

while True:
    nx = a + dx[d]
    ny = b + dy[d]
    if is_visited[nx][ny] == 0 and :
        is_visited[nx][ny] = 1
        a, b = nx, ny
        continue
