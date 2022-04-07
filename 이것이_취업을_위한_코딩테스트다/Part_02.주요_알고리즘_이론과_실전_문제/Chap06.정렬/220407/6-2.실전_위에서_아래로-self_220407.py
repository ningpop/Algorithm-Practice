# 2022.04.07
# 제한 시간 15분 / 풀이 시간 2분 25초
# 채점 결과: 정답
# 시간복잡도: O(N)

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

array.sort(reverse=True)
for num in array:
    print(num, end=' ')