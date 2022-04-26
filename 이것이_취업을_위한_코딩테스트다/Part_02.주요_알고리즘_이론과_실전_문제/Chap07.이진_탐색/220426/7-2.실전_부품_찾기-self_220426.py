# 2022.04.26
# 제한 시간 30분 / 풀이 시간 7분 00초
# 채점 결과: 정답
# 시간복잡도: O(N)

n = int(input())
storage = list(map(int, input().split()))
m = int(input())
needs = list(map(int, input().split()))

storage_table = [0] * (max(storage) + 1)
for i in storage:
    storage_table[i] += 1

for i in needs:
    if storage_table[i] != 0:
        print('yes', end=' ')
    else:
        print('no', end=' ')