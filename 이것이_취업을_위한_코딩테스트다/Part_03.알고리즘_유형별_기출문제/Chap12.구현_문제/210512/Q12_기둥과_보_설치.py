# 2021.05.18
# 제한시간 50분
# 시간초과 및 미해결
# https://programmers.co.kr/learn/courses/30/lessons/60061

def solution(n: int, build_frame: list) -> list:
    answer = [[]]
    return answer

print(solution(5, [
    [1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], 
    [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]
    ]))
print(solution(5, [
    [0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], 
    [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], 
    [1, 1, 1, 0], [2, 2, 0, 1]
    ]))