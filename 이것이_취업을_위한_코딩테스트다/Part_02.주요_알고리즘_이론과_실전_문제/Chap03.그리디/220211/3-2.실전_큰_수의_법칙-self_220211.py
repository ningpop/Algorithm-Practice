# 2022.02.11
# 제한 시간 30분 / 풀이 시간 13분 37초
# 채점 결과: 정답

N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort(reverse=True)

result = 0
max_count = K
for i in range(M):
    if max_count == 0:
        result += num_list[1]
        max_count = K
    else:
        result += num_list[0]
        max_count -= 1

print(result)