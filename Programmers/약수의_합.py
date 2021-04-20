def solution(n: int) -> int:
    answer = 0
    for i in range(1, n + 1):
        if n%i == 0:
            answer += i
    return answer

if __name__ == "__main__":
    print(solution(12))
    print(solution(5))