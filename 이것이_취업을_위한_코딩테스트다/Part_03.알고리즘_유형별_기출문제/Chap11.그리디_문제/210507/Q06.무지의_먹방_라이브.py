# 본 문제는 풀이 시간 내에 풀지 못했다

# 프로그래머스 채점 결과
# 정확성 테스트: 17개 / 32개 (22.8점 / 100점)
# 효율성 테스트: 0개 / 8개 (0점 / 100점)

def solution(food_times: list, k: int) -> int:
    answer = 0
    while True:
        if answer == len(food_times):
            answer = 0
        if not food_times and k > 0:
            return -1
        if k == 0:
            break
        
        if food_times[answer] == 0:
            answer += 1
            continue
        food_times[answer] -= 1

        answer += 1
        k -= 1
    return answer+1

print(solution([3, 1, 2], 5))