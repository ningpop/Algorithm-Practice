# 2022.03.03
# 제한 시간 30분 / 풀이 시간 7분 30초
# 채점 결과: 정답
# 시간복잡도: O(N)

n, k = map(int, input().split())

count = 0
while n > 1:
    if n % k == 0:
        n //= k
    else:
        n -= 1
    count += 1

print(count)