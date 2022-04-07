# 2022.04.07
# 제한 시간 20분 / 풀이 시간 5분 53초
# 채점 결과: 정답
# 시간복잡도: O(N)

n, k = map(int, input().split())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

for i in range(k):
    min_value_a = min(array_a)
    max_value_b = max(array_b)

    if min_value_a < max_value_b:
        array_a.append(max_value_b)
        array_b.append(min_value_a)
        array_a.remove(min_value_a)
        array_b.remove(max_value_b)

print(sum(array_a))