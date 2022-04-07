# 2022.04.07
# 제한 시간 20분 / 풀이 시간 02분 14초
# 채점 결과: 정답
# 시간복잡도: O(N)

n = int(input())

array = []
for _ in range(n):
    name, score = input().split()
    array.append((name, int(score)))

array.sort(key=lambda x : x[1])
for student in array:
    print(student[0], end=' ')