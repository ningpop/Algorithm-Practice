# 2022.02.11
# 제한 시간 30분 / 풀이 시간 06분 00초
# 채점 결과: 정답
# 시간복잡도: O(N)

N, K = map(int, input().split())

count = 0
while N > 1:
    if N % K == 0:
        N = int(N / K)
        count += 1
    else:
        N -= 1
        count += 1

print(count)