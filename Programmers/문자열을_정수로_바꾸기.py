def solution(s):
    if s[0] != '-':
        return int(s)
    answer = int(s[1:])
    answer = -answer
    return answer

if __name__ == "__main__":
    print(solution('1234'))
    print(solution('-1234'))