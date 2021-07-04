# 2021.07.04
# 풀이시간 30분 / 제한시간 40분
# 정답

import heapq

INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)

distance = distance[1:]
print(distance.index(max(distance)) + 1, max(distance), end=' ')
count = 0
for i in distance:
    if max(distance) == i:
        count += 1
print(count)