# 2022.02.13
# 제한 시간 30분 / 풀이 시간 42분 50초
# 채점 결과: 시간 초과 및 오답
# 시간복잡도: 

from collections import deque

n, m = map(int, input().split())

miro = []
for i in range(n):
    row = list(map(int, input()))
    miro.append(row)

visited = [ [ False for j in range(m) ] for i in range(n) ]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 0
    while queue:
        value = queue.popleft()
        print(value)
        count += 1
        if value == (n, m):
            break
        for i in range(len(dx)):
            nx = value[0] + dx[i]
            ny = value[1] + dy[i]
            if nx < 0 or ny < 0 or nx > n or ny > m:
                continue
            if not visited[nx][ny] and miro[nx][ny] == 1:
                print('miro: ', nx, ny)
                queue.append((nx, ny))
    return count

print(bfs(0, 0))