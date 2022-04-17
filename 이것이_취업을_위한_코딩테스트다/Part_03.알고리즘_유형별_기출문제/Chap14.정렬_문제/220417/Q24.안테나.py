# 2022.04.17
# 제한 시간 20분 / 풀이 시간 30분 00초
# 채점 결과: 오답, 제한 시간 내 미해결
# 시간복잡도: O(logN)
# 문제 링크: https://www.acmicpc.net/problem/18310

n = int(input())
houses = list(map(int, input().split()))

houses.sort()
center = 0

while True:
    start = houses[0]
    end = houses[-1]
    center = (start + end) // 2

    if center in houses:
        break
    
    pre_houses = [ num for num in houses if num < center ]
    post_houses = [ num for num in houses if num > center ]
    if len(pre_houses) < len(post_houses):
        houses = post_houses
    else:
        houses = pre_houses

print(center)