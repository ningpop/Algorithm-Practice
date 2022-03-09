# 2022.03.09
# 제한 시간 30분 / 풀이 시간 10분 01초
# 채점 결과: 정답
# 시간복잡도: O(N)

from collections import deque

n = int(input())
people = list(map(int, input().split()))

people.sort(reverse=True)

group = 0
people = deque(people)
while people:
    horror = people.popleft()
    for i in range(horror - 1):
        people.popleft()
    group += 1

print(group)