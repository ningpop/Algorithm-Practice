# 2022.04.18
# 제한 시간 20분 / 풀이 시간 50분 00초
# 채점 결과: 정답, 제한 시간 내 미해결
# 시간복잡도: O(N^2)
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N: int, stages: list) -> list:
    status = sorted(stages, reverse=True)

    result = []
    for stage in range(1, N + 1):
        clear_count = 0
        people = len(status)
        while status:
            if status[-1] == stage:
                clear_count += 1
                status.pop()
            else:
                break
        rate = 0
        if people != 0:
            rate = clear_count / people
        result.append((stage, rate))
    return [ i[0] for i in sorted(result, key=lambda x : (-x[1], x[0]))]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # [3,4,2,1,5]
print(solution(4, [4, 4, 4, 4, 4])) # [4,1,2,3]
print(solution(3, [1, 1, 1])) # [1,2,3]