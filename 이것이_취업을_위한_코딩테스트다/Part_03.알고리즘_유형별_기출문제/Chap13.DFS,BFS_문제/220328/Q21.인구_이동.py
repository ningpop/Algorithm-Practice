# 2022.04.04
# 제한 시간 40분 / 풀이 시간 42분 00초
# 채점 결과: 오답 및 제한시간 내 미해결
# 시간복잡도: 
# 문제 링크: https://www.acmicpc.net/problem/16234

n, l, r = map(int, input().split())
world = []
for _ in range(n):
    world.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

count = 0
while True:
    union_list = []
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                distance = abs(world[i][j] - world[nx][ny])
                if l <= distance <= r:
                    if (i, j) not in union_list:
                        union_list.append((i, j))
    if not union_list:
        break

    print(union_list)
    result = 0
    for country_x, country_y in union_list:
        result += world[country_x][country_y]
    print(f'합: {result}, 개수: {len(union_list)}')
    result //= len(union_list)
    print(f'평균: {result}')
    for country_x, country_y in union_list:
        world[country_x][country_y] = result
    count += 1
    print(world)

print(count)