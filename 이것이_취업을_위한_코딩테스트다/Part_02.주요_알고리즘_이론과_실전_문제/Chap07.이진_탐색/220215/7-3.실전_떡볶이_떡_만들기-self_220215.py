# 2022.02.15
# 제한 시간 40분 / 풀이 시간 40분 00초
# 채점 결과: 시간 초과 및 오답
# 시간복잡도: O(NlogN)

import sys

def inputLine() -> str:
    return sys.stdin.readline().rstrip()

def cut_rice_cake(rice_cake, height):
    result = 0
    for i in rice_cake:
        result += (i - height)
    return result

def binary_search(rice_cake, m, start, end):
    while start <= end:
        mid = (start + end) // 2
        if cut_rice_cake(rice_cake[mid:], rice_cake[mid]) == m:
            return mid
        elif cut_rice_cake(rice_cake[mid:], rice_cake[mid]) > m:
            end = mid - 1
        else:
            start = mid + 1
    return mid

n, m = map(int, inputLine().split())
rice_cake = list(map(int, inputLine().split()))

rice_cake.sort()
index = binary_search(rice_cake, m, 0, n - 1)
print(rice_cake[index])