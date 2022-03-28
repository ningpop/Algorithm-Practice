# 2021.05.29
# 풀이시간 40분 / 제한시간 40분
# 제한시간 초과 및 미해결
# https://www.acmicpc.net/problem/16234

n, l, r = map(int, input().split())
country = []
for _ in range(n):
    country.append(list(map(int, input().split())))

def is_opened(x: tuple, y: tuple) -> bool:
    result = country[x[0]][x[1]] - country[y[0]][y[1]]
    if result < 0:
        result = -result
    
    if l <= result <= r:
        return True
    return False

