# 2021.07.04
# 풀이시간 40분 / 제한시간 40분
# 제한시간 초과 및 미해결

import heapq

INF = int(1e9)

t = int(input())

while t:
    n = int(input())
    graph = [[] for i in range(n + 1)]
    

    t -= 1