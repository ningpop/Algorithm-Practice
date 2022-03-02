# 2022.03.03
# 제한 시간 30분 / 풀이 시간 5분 12초
# 채점 결과: 정답
# 시간복잡도: O(N)

n, m = map(int, input().split())

cards = []
for _ in range(n):
    cards.append(list(map(int, input().split())))

num = 0
for row in cards:
    num = max(num, min(row))

print(num)