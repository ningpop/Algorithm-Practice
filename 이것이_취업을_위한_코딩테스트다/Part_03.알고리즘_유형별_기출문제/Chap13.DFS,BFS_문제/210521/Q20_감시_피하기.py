# 2021.05.27
# 풀이시간 60분 / 제한시간 60분
# 제한시간 초과
# https://www.acmicpc.net/problem/18428

n = int(input())
school = []
for _ in range(n):
    school.append(list(input().split()))
temp = [['X'] * n for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

#print(school)

dx = []
dy = []
for i in range(1, n + 1):
    for j in [-1, 0, 1, 0]:
        dx.append(i * j)
for i in range(1, n + 1):
    for j in [0, 1, 0, -1]:
        dx.append(i * j)

# result = 

def scanning(x, y):
    for i in range(4 * n):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if temp[nx][ny] == 'X':
                temp[nx][ny] = 'O'
                scanning(nx, ny)

def dfs(count):
    global data
    if count == 3:
        for i in range(n):
            for j in range(n):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(n):
                if temp[i][j] == 'O':
                    scanning(i, j)
        return data
    for i in range(n):
        for j in range(n):
            if school[i][j] == 'X':
                school[i][j] = 'O'
                count += 1
                dfs(count)
                school[i][j] = 'X'
                count -= 1

print(dfs(0))
