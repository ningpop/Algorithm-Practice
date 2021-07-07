# 2021.07.07
# 풀이시간 5분 / 제한시간 30분
# 정답

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

start = bisect_left(array, x)
end = bisect_right(array, x)

count = 0
for _ in range(start, end):
    count += 1

if count == 0:
    print(-1)
else:
    print(count)