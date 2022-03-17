# 2022.03.18
# 제한 시간 30분 / 풀이 시간 분 초
# 채점 결과: 오답 및 제한시간 내 미해결
# 시간복잡도: 
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s: str) -> int:
    length = len(s)

    result = length
    for i in range(1, length // 2):
        char_count = 1
        completed = ''
        for j in s:
            




        
        result = min(result, len(completed))

    return result

print(solution("aabbaccc")) # 7
print(solution("ababcdcdababcdcd")) # 9
print(solution("abcabcdede")) # 8
print(solution('abcabcabcabcdededededede')) # 14
print(solution('xababcdcdababcdcd')) # 17