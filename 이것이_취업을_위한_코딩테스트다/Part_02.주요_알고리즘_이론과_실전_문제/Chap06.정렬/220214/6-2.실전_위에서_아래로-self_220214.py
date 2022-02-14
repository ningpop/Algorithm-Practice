# 2022.02.14
# 제한 시간 15분 / 풀이 시간 01분 20초
# 채점 결과: 정답
# 시간복잡도: O(N)

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

for i in array:
    print(i, end=' ')