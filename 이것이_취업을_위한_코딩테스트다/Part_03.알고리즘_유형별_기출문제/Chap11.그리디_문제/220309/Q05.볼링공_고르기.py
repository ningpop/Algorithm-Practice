# 2022.03.13
# 제한 시간 30분 / 풀이 시간 8분 58초
# 채점 결과: 정답
# 시간복잡도: O(N)이하

from itertools import combinations

n, m = map(int, input().split())
ball = list(map(int, input().split()))

ball_index_list = [ i  for i in range(0, n) ]
comb_list = list(combinations(ball_index_list, 2))

result = 0
for (i, j) in comb_list:
    if ball[i] != ball[j]:
        result += 1

print(result)