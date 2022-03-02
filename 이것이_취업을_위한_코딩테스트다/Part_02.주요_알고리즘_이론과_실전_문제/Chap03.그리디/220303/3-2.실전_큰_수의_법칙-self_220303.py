# 2022.03.03
# 제한 시간 30분 / 풀이 시간 08분 32초
# 채점 결과: 정답
# 시간복잡도: O(M)

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)

result = 0
count = 0
for i in range(m):
    if count >= k:
        result += numbers[1]
        count = 0
    else:
        result += numbers[0]
        count += 1

print(result)