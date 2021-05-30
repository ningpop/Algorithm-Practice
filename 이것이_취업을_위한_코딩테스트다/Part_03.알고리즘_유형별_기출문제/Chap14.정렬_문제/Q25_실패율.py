# 2021.05.30
# 풀이시간 20분 / 제한시간 20분
# 제한시간 초과 및 일부 테스트 케이스 런타임 오류로 인한 미해결 (70.4점)
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N: int, stages: list) -> list:
    answer = []
    for i in range(1, N + 1):
        total_count = 0
        count = 0
        for j in stages:
            if i <= j:
                total_count += 1
            if i == j:
                count += 1
        answer.append((i, count / total_count))
    answer.sort(key=lambda x: (-x[1], x[0]))
    return [i[0] for i in answer]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # [3,4,2,1,5]
print(solution(4, [4,4,4,4,4])) # [4,1,2,3]