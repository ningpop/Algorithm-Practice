# 2022.03.15
# 제한 시간 30분 / 풀이 시간 30분 30초
# 채점 결과: 오답 및 제한시간 내 미해결
# 시간복잡도: 

n = int(input())
coin = list(map(int, input().split()))

''' 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)
'''