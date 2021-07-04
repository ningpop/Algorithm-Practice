# 2021.07.04
# 풀이시간 34분 / 제한시간 40분
# 정답

INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for k in range(1, n + 1):
    count = 0
    for a in range(1, n + 1):
        if graph[k][a] != INF and graph[k][a] != 0:
            count += 1
    for b in range(1, n + 1):
        if graph[b][k] != INF and graph[b][k] != 0:
            count += 1
    if count == 5:
        result += 1

print(result)

# 데이터 확인용 출력 코드
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if graph[i][j] == INF:
#             print('X', end=' ')
#         else:
#             print(graph[i][j], end=' ')
#     print()