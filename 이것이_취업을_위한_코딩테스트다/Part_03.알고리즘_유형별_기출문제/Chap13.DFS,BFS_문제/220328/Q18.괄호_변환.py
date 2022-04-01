# 2022.04.02
# 제한 시간 20분 / 풀이 시간 20분 00초
# 채점 결과: 오답, 제한 시간 내 미해결
# 시간복잡도: 
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/60058

def is_correct_string(p: str) -> bool:
    stack = []
    for i in p:
        if i == "(":
            stack.append(i)
        elif i == ")":
            stack.pop()
    if not stack:
        return True
    return False

def solution(p: str) -> str:
    if p == "":
        return ""
    
    if is_correct_string(p):
        is_balanced = 0
        u = v = ""
        for idx, val in enumerate(p):
            if val == "(":
                is_balanced += 1
            elif val == ")":
                is_balanced -= 1
            
            if is_balanced == 0:
                u = p[:idx + 1]
                v = p[idx + 1:]
                break
        solution(v)
    else:
        temp = "(" + solution(v) + ")"


    answer = ''
    return answer

print(solution("(()())()"))     # (()())()
# print(solution(")("))           # ()
# print(solution("()))((()"))     # ()(())()