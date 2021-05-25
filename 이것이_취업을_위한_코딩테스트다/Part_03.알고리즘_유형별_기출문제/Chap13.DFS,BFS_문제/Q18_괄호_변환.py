# 2021.05.225
# 풀이시간 20분 / 제한시간 20분
# 제한시간 초과 및 미해결
# https://programmers.co.kr/learn/courses/30/lessons/60058

p = input()

def is_corrected(string: str) -> bool:
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        else:
            if stack[-1] == i:
                return False
    if not stack:
        return True
    return False


def dfs(s: str) -> str:
    if not s:
        return ''
    
    pass

