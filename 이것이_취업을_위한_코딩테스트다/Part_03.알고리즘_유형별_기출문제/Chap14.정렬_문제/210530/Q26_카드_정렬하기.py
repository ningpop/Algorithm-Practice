# 2021.05.30
# 풀이시간 30분 / 제한시간 30분
# 제한시간 초과 및 미해결
# https://www.acmicpc.net/problem/1715

n = int(input())
card = []
for _ in range(n):
    card.append(int(input()))

card.sort()
answer = card[0] + card[1]
for i in card[2:]:
    temp = answer + i
    answer += temp

print(answer)