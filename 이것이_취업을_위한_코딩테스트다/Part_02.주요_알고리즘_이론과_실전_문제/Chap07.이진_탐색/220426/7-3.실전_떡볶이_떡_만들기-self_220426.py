# 2022.04.26
# 제한 시간 40분 / 풀이 시간 15분 38초
# 채점 결과: 정답
# 시간복잡도: O(logN)

def cutting(dduk: list, line: int) -> int:
    d = 0
    for i in dduk:
        etc = i - line
        if etc > 0:
            d += etc
    return d

n, m = map(int, input().split())
dduk = list(map(int, input().split()))

start = 0
end = max(dduk)
answer = -1
while start <= end:
    mid = (start + end) // 2
    result = cutting(dduk, mid)
    if result == m:
        answer = mid
        break
    elif result < m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)