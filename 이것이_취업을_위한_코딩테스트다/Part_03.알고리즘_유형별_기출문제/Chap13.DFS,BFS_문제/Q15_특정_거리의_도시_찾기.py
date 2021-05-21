# 2021.05.21
# 제한시간 30분
# 시간초과 및 미해결
# https://www.acmicpc.net/problem/18352

def dfs(country: list, n: int, shorts: list, N: int):
    for i in country[n]:
        if shorts[i] == N:
            shorts[i] = 1
        else:
            pass

N, M, K, X = map(int, input().split())

country = [[] for _ in range(N+1)]
for _ in range(N):
    A, B = map(int, input().split())
    country[A].append(B)

shorts = [ N for _ in range(N+1)]

#print(dfs())