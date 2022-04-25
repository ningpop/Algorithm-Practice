# 2022.04.25
# 제한 시간 30분 / 풀이 시간 30분 00초
# 채점 결과: 오답, 제한 시간 내 미해결
# 시간복잡도: O(N)
# 문제 링크: https://www.acmicpc.net/problem/1715

n = int(input())

cards = []
for _ in range(n):
    cards.append(int(input()))

cards.sort()
result = 0
m = len(cards)
for i in range(m):
    count = (m - i) * cards[i]
    result += count
result -= cards[0]

print(result)