# 2022.03.28
# 제한 시간 30분 / 풀이 시간 42분 16초
# 채점 결과: 오답(시간초과), 제한 시간 내 미해결
# 시간복잡도: 
# 문제 링크: https://www.acmicpc.net/problem/18352

def dfs(x: int, d: int, count: int):
    if cities[d] == []:
        min_roads[d] = min(min_roads[d], count + 1)
        return
    for i in cities[d]:
        dfs(x, i, count + 1)

n, m, k, x = map(int, input().split())

cities = [ [] for i in range(n + 1) ]
for _ in range(m):
    source, destination = map(int, input().split())
    cities[source].append(destination)

min_roads = {}
for i in range(1, n + 1):
    min_roads[i] = 1e9

for i in cities[x]:
    min_roads[i] = min(min_roads[i], 1)
    dfs(x, i, 0)

if k not in min_roads.values():
    print(-1)
else:
    for key, value in min_roads.items():
        if value == k:
            print(key)