# 2021.05.13
# 제한시간 30분
# 시간초과 및 미해결

def solution(s: str) -> int:
    word = 1
    result = 1000
    while True:
        pre = s[:word]
        count = 0
        for i in range(word, len(s), word):
            if s[i:i+word] == pre:
                count += 1
        word += 1
        
        
        if word > len(s):
            break

print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))