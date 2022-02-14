# 2022.02.14
# 제한 시간 20분 / 풀이 시간 05분 38초
# 채점 결과: 오답
# 시간복잡도: O(N)

n, k = map(int, input().split())

array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

array_a.sort()
array_b.sort(reverse=True)

for i in range(k):
    array_a[i], array_b[i] = array_b[i], array_a[i]

result = 0
for i in array_a:
    result += i

print(result)