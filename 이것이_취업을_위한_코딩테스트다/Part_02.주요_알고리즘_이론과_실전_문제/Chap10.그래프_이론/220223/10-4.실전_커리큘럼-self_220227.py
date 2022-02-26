# 2022.02.27
# 제한 시간 50분 / 풀이 시간 28분 26초
# 채점 결과: 정답
# 시간복잡도: O(N^2)

n = int(input())
indegree = [0] * (n + 1)
table = [0] * (n + 1)

for i in range(1, n + 1):
    time_and_pre_lecture = list(map(int, input().split()))
    time = time_and_pre_lecture[0]
    table[i] = time
    pre_lecture = time_and_pre_lecture[1:-1]
    indegree[i] += time
    max_time = 0
    for j in pre_lecture:
        max_time = max(max_time, indegree[j])
    indegree[i] += max_time

for i in range(1, n + 1):
    print(indegree[i])