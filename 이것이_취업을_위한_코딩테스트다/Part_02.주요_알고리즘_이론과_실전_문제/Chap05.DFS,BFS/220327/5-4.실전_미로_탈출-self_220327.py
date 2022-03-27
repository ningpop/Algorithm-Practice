# 2022.03.27
# 제한 시간 30분 / 풀이 시간 26분 38초
# 채점 결과: 정답
# 시간복잡도: O(N)...?
# 문제 링크: 

from collections import deque

n, m = map(int, input().split())
miro = [ [0] * (m + 1) ]
for _ in range(n):
    row = [ int(i) for i in input() ]
    miro.append([0] + row)

is_visited = [ [0] * (m + 1) for _ in range(n + 1) ]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque([(1, 1)])
while q:
    x, y = q.popleft()
    is_visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 1 <= nx <= n and 1 <= ny <= m:
            if miro[nx][ny] == 1 and is_visited[nx][ny] == 0:
                q.append((nx, ny))
                miro[nx][ny] = miro[x][y] + 1

print(miro[n][m])